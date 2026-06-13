
let allColleges = [];
let bookmarks = JSON.parse(localStorage.getItem('cet_bookmarks') || '[]');
let compareList = [];
let currentSort = 'score';

async function getRecommendations() {
    const percentile = document.getElementById('percentile').value;
    const branch     = document.getElementById('branch').value;
    const city       = document.getElementById('city').value;
    const max_fees   = document.getElementById('max_fees').value;
    const priority   = document.getElementById('priority').value;
    
    if (!percentile || !branch) { showError('Please enter your percentile and select a branch!'); return; }

    showLoading(true); hideError();
    document.getElementById('results').style.display = 'none';

    try {
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                percentile: parseFloat(percentile), branch,
                city: city || null,
                max_fees: max_fees ? parseInt(max_fees) : null,
                priority
            })
        });
        const data = await response.json();
        showLoading(false);
        if (data.error) { showError(data.error); return; }

        allColleges = data.colleges;
       
       if (allColleges.length === 0) { 
    showError(`No colleges found for ${branch} in ${city || 'any city'} with ${percentile} percentile. Try: Higher percentile, Different city, or "Any City" option.`); 
    return; 
}
        renderResults(branch);
    } catch(err) {
        showLoading(false);
       showError('No colleges found! Tips: Try higher percentile, select "Any City", or try different branch.');
    }
}

function renderResults(branch) {
    const sorted = getSorted(allColleges, currentSort);
    const list = document.getElementById('colleges-list');
    document.getElementById('results-title').textContent = `Recommended Colleges — ${branch}`;
    document.getElementById('results-count').textContent = `${sorted.length} Found`;
    list.innerHTML = '';

    sorted.forEach((college, index) => {
        const isBookmarked = bookmarks.some(b => b.college_name === college.college_name && b.branch === college.branch);
        const isComparing  = compareList.some(c => c.college_name === college.college_name);
        const scoreP = Math.round(college.score * 100);

        // Cutoff trend bars
       // Cutoff trend bars
const c21 = parseFloat(college.cutoff_2022) || 0;
const c22 = parseFloat(college.cutoff_2023) || 0;
const c23 = parseFloat(college.cutoff_2024) || 0;
const minC = Math.min(c21, c22, c23);
const maxC = Math.max(c21, c22, c23);
const range = (maxC - minC) || 1;
const h21 = Math.round(((c21 - minC) / range) * 34) + 10;
const h22 = Math.round(((c22 - minC) / range) * 34) + 10;
const h23 = Math.round(((c23 - minC) / range) * 34) + 10;
        
        const card = document.createElement('div');
        card.className = `college-card ${isBookmarked ? 'bookmarked' : ''}`;
        card.style.animationDelay = `${index * 0.06}s`;
        card.innerHTML = `
            <div class="card-top">
                <div class="card-left">
                    <div class="rank-badge"><i class="fa-solid fa-trophy"></i> Rank #${index + 1}</div>
                    <div class="college-name">${college.college_name}</div>
                    <div class="college-meta">
                       <span class="meta-tag"><i class="fa-solid fa-location-dot"></i> ${college.city}</span>
<span class="meta-tag"><i class="fa-solid fa-graduation-cap"></i> ${college.branch}</span>
${college.hostel === 'Yes' ? '<span class="meta-tag hostel-tag"><i class="fa-solid fa-house"></i> Hostel</span>' : ''}
                    </div>
                </div>
                <div class="card-actions">
                    <button class="action-btn ${isBookmarked ? 'bookmarked-btn' : ''}"
    onclick="toggleBookmark('${college.college_name}','${college.branch}',${index})"
    title="Save College"><i class="fa-${isBookmarked ? 'solid' : 'regular'} fa-bookmark"></i></button>
<button class="action-btn ${isComparing ? 'bookmarked-btn' : ''}"
    onclick="toggleCompare(${index})"
    title="Compare"><i class="fa-solid fa-scale-balanced"></i></button>
                </div>
            </div>

            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-label">Cutoff 2023</div>
                    <div class="stat-value purple">${college.cutoff_2023}%</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Fees / Year</div>
                    <div class="stat-value">₹${(college.fees/100000).toFixed(1)}L</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Avg Package</div>
                    <div class="stat-value green">₹${(college.avg_package/100000).toFixed(1)}L</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Rating</div>
                    <div class="stat-value"><i class="fa-solid fa-star" style="color:#FFB347;"></i> ${college.rating}</div>
                </div>
            </div>

            <div class="score-section">
               <div class="score-row"><span>AI Match Score</span><span>${scoreP}%</span></div>
                <div class="score-bar"><div class="score-fill" style="width:${scoreP}%"></div></div>
            </div>

            <div class="trend-section">
                <div class="trend-title"><i class="fa-solid fa-chart-line"></i> Cutoff Trend (2021 → 2023)</div>
                <div class="trend-bars">
                    <div class="trend-bar-wrap">
    <div class="trend-val">${c21 || 'N/A'}</div>
    <div class="trend-bar" style="height:${h21}px"></div>
    <div class="trend-year">2022</div>
</div>
<div class="trend-bar-wrap">
    <div class="trend-val">${c22 || 'N/A'}</div>
    <div class="trend-bar" style="height:${h22}px"></div>
    <div class="trend-year">2023</div>
</div>
<div class="trend-bar-wrap">
    <div class="trend-val current">${c23 || 'N/A'}</div>
    <div class="trend-bar current" style="height:${h23}px"></div>
    <div class="trend-year">2024</div>
</div>
                </div>
            </div>
        `;
        list.appendChild(card);
    });

    document.getElementById('results').style.display = 'block';
    updateBookmarksUI();
}

function getSorted(colleges, sortBy) {
    const arr = [...colleges];
    if (sortBy === 'score')   return arr.sort((a,b) => b.score - a.score);
    if (sortBy === 'fees')    return arr.sort((a,b) => a.fees - b.fees);
    if (sortBy === 'package') return arr.sort((a,b) => b.avg_package - a.avg_package);
    if (sortBy === 'cutoff')  return arr.sort((a,b) => b.cutoff_2023 - a.cutoff_2023);
    return arr;
}

function sortResults(by, btn) {
    currentSort = by;
    document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const branch = document.getElementById('branch').value;
    renderResults(branch);
}

function toggleBookmark(name, branch, index) {
    const existing = bookmarks.findIndex(b => b.college_name === name && b.branch === branch);
    if (existing >= 0) {
        bookmarks.splice(existing, 1);
    } else {
        const college = getSorted(allColleges, currentSort)[index];
        bookmarks.push(college);
    }
    localStorage.setItem('cet_bookmarks', JSON.stringify(bookmarks));
    const branch2 = document.getElementById('branch').value;
    renderResults(branch2);
}

function updateBookmarksUI() {
    const section = document.getElementById('bookmarks-section');
    const list    = document.getElementById('bookmarks-list');
    if (bookmarks.length === 0) { section.style.display = 'none'; return; }
    section.style.display = 'block';
    list.innerHTML = bookmarks.map((b,i) => `
    <div class="bookmark-item">
        <i class="fa-solid fa-school"></i> ${b.college_name}
        <button onclick="removeBookmark(${i})"><i class="fa-solid fa-xmark"></i></button>
    </div>`).join('');
}

function removeBookmark(i) {
    bookmarks.splice(i,1);
    localStorage.setItem('cet_bookmarks', JSON.stringify(bookmarks));
    updateBookmarksUI();
    if (allColleges.length > 0) renderResults(document.getElementById('branch').value);
}

function toggleCompare(index) {
    const college = getSorted(allColleges, currentSort)[index];
    const existing = compareList.findIndex(c => c.college_name === college.college_name);
    if (existing >= 0) {
        compareList.splice(existing, 1);
    } else {
        if (compareList.length >= 3) { showError('Maximum 3 colleges can be compared at once!'); return; }
        compareList.push(college);
    }
    updateCompareBar();
    renderResults(document.getElementById('branch').value);
}

function updateCompareBar() {
    const bar = document.getElementById('compare-bar');
    const chips = document.getElementById('compare-chips');
    if (compareList.length === 0) { bar.style.display = 'none'; return; }
    bar.style.display = 'block';
   chips.innerHTML = compareList.map((c,i) => `
    <div class="compare-chip">
        <i class="fa-solid fa-building-columns"></i> ${c.college_name.split(' ')[0]}
        <button onclick="removeCompare(${i})"><i class="fa-solid fa-xmark"></i></button>
    </div>`).join('');
}

function removeCompare(i) {
    compareList.splice(i,1);
    updateCompareBar();
    if (allColleges.length > 0) renderResults(document.getElementById('branch').value);
}

function clearCompare() { compareList = []; updateCompareBar(); if (allColleges.length > 0) renderResults(document.getElementById('branch').value); }

function showCompareModal() {
    if (compareList.length < 2) { showError('Select at least 2 colleges to compare!'); return; }
    const content = document.getElementById('compare-content');
    const fields = [
        ['College', c => c.college_name],
        ['City', c => c.city],
        ['Cutoff 2023', c => c.cutoff_2023 + '%'],
        ['Fees/Year', c => '₹' + (c.fees/100000).toFixed(1) + 'L'],
        ['Avg Package', c => '₹' + (c.avg_package/100000).toFixed(1) + 'L'],
        ['Rating', c => c.rating + ' ★'],
        ['Hostel', c => c.hostel],
        ['AI Score', c => Math.round(c.score*100) + '%'],
    ];
    content.innerHTML = `<table class="compare-table">
        ${fields.map(([label, fn]) => {
            const vals = compareList.map(fn);
            const isNum = fields.indexOf([label,fn]) > 0;
            return `<tr>
                <th>${label}</th>
                ${compareList.map((c,i) => `<td class="${vals[i] === vals.reduce((a,b) => a > b ? a : b) && isNum ? 'highlight' : ''}">${fn(c)}</td>`).join('')}
            </tr>`;
        }).join('')}
    </table>`;
    document.getElementById('modal-overlay').style.display = 'block';
}

function closeModal(e) {
    if (!e || e.target === document.getElementById('modal-overlay'))
        document.getElementById('modal-overlay').style.display = 'none';
}

function shareResults() {
    const url = window.location.href;
    navigator.clipboard.writeText(url).then(() => {
        const toast = document.getElementById('share-toast');
        toast.style.display = 'block';
        setTimeout(() => toast.style.display = 'none', 2500);
    });
}

function showLoading(show) {
    document.getElementById('loading').style.display = show ? 'block' : 'none';
    document.getElementById('btn').disabled = show;
    document.getElementById('btn').innerHTML = show ? 
        '<i class="fa-solid fa-spinner fa-spin"></i> Finding...' : 
        '<i class="fa-solid fa-wand-magic-sparkles"></i> Find My Colleges';
}
function showError(msg) { const e = document.getElementById('error'); e.textContent = '⚠️ ' + msg; e.style.display = 'block'; }
function hideError() { document.getElementById('error').style.display = 'none'; }

// Load bookmarks on start
updateBookmarksUI();
