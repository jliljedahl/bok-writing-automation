/**
 * NOIR Dashboard Data Loader
 * Laddar och renderar bokprojektdata
 */

// Load data from JSON file
async function loadDataFromFile() {
    try {
        // Try to load data.json from same directory
        const response = await fetch('data.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Kunde inte ladda data från data.json:', error);
        console.log('Använder demo data istället...');
        return getDemoData();
    }
}

// Demo data if no JSON file found
function getDemoData() {
    return {
        title: "Demo Projekt",
        author: "Författare",
        currentPhase: "Inte startad",
        structure: "Ej vald",
        targetWords: 80000,
        totalWords: 0,
        lastUpdated: new Date().toISOString(),
        outline: null,
        characters: [],
        chapters: initializeDemoChapters(12)
    };
}

// Initialize demo chapters
function initializeDemoChapters(count) {
    const chapters = [];
    for (let i = 1; i <= count; i++) {
        chapters.push({
            number: i,
            title: `Kapitel ${i}`,
            status: 'pending',
            words: 0,
            quality: null,
            tension: null,
            lastUpdated: null,
            synopsis: "",
            versions: [],
            metadata: {}
        });
    }
    return chapters;
}

// Render outline
function renderOutline(outline) {
    const container = document.getElementById('outline-content');

    if (!outline) {
        container.innerHTML = `
            <div class="alert alert-warning">
                <strong>⚠️ Ingen outline ännu:</strong> Kör Fas 0 (Narrative Validation) för att generera outline.
            </div>
        `;
        return;
    }

    let html = `
        <div class="outline-section">
            <h3>Logline</h3>
            <p>${outline.logline || 'Ingen logline ännu'}</p>
        </div>

        <div class="outline-section">
            <h3>Hook</h3>
            <p>${outline.hook || 'Ingen hook ännu'}</p>
        </div>

        <div class="outline-section">
            <h3>Twist</h3>
            <p>${outline.twist || 'Ingen twist ännu'}</p>
        </div>

        <div class="outline-section">
            <h3>Resolution</h3>
            <p>${outline.resolution || 'Ingen resolution ännu'}</p>
        </div>
    `;

    if (outline.acts && outline.acts.length > 0) {
        html += '<h2>Akter</h2>';
        outline.acts.forEach(act => {
            html += `
                <div class="act-section">
                    <div class="act-title">${act.title}</div>
                    <p>${act.description}</p>
            `;

            if (act.beats && act.beats.length > 0) {
                html += '<h4>Plot Beats</h4>';
                act.beats.forEach(beat => {
                    html += `
                        <div class="beat-item">
                            <strong>${beat.name}</strong>
                            ${beat.chapter ? `<span style="color: var(--muted)"> (Kapitel ${beat.chapter})</span>` : ''}
                            <p>${beat.description}</p>
                        </div>
                    `;
                });
            }

            html += '</div>';
        });
    }

    container.innerHTML = html;
}

// Render characters
function renderCharacters(characters) {
    const container = document.getElementById('characters-content');

    if (!characters || characters.length === 0) {
        container.innerHTML = `
            <div class="alert alert-warning">
                <strong>⚠️ Inga karaktärer ännu:</strong> Karaktärer skapas i Fas 1 (Creative Planning) av Morgan.
            </div>
        `;
        return;
    }

    let html = '';
    characters.forEach(char => {
        html += `
            <div class="character-card">
                <div class="character-header">
                    <div class="character-name">${char.name}</div>
                    <div class="character-role">${char.role}</div>
                </div>

                <p><strong>Ålder:</strong> ${char.age || 'Okänd'}</p>
                <p><strong>Yrke:</strong> ${char.occupation || 'Okänt'}</p>
                <p><strong>Beskrivning:</strong> ${char.description || 'Ingen beskrivning'}</p>

                ${char.arc ? `
                    <h4>Character Arc</h4>
                    <p><strong>Start:</strong> ${char.arc.start}</p>
                    <p><strong>Mitt:</strong> ${char.arc.middle}</p>
                    <p><strong>Slut:</strong> ${char.arc.end}</p>
                ` : ''}

                ${char.ghost ? `<p><strong>Ghost:</strong> ${char.ghost}</p>` : ''}
                ${char.want ? `<p><strong>Want:</strong> ${char.want}</p>` : ''}
                ${char.need ? `<p><strong>Need:</strong> ${char.need}</p>` : ''}
            </div>
        `;
    });

    container.innerHTML = html;
}

// Render chapters list
function renderChaptersList(chapters) {
    const container = document.getElementById('chapters-list');

    if (!chapters || chapters.length === 0) {
        container.innerHTML = `
            <div class="alert alert-info">
                <strong>ℹ️ Inga kapitel ännu:</strong> Kapitel skrivs i Fas 2-4 av Writing Team och Quality Team.
            </div>
        `;
        return;
    }

    let html = '';
    chapters.forEach(chapter => {
        const statusClass = chapter.status === 'completed' ? 'status-completed' :
                          chapter.status === 'in-progress' ? 'status-in-progress' : 'status-pending';
        const statusText = chapter.status === 'completed' ? 'Klar' :
                          chapter.status === 'in-progress' ? 'Pågår' : 'Väntande';

        html += `
            <div class="card" style="cursor: pointer;" onclick="openChapterModal(${chapter.number})">
                <h3>${chapter.title}</h3>
                <div class="metadata">
                    <div class="metadata-item">
                        <div class="metadata-label">Status</div>
                        <div class="metadata-value">
                            <span class="status-badge ${statusClass}">${statusText}</span>
                        </div>
                    </div>
                    <div class="metadata-item">
                        <div class="metadata-label">Ord</div>
                        <div class="metadata-value">${chapter.words.toLocaleString('sv-SE')}</div>
                    </div>
                    <div class="metadata-item">
                        <div class="metadata-label">Kvalitet</div>
                        <div class="metadata-value">${chapter.quality ? chapter.quality + '/10' : '-'}</div>
                    </div>
                    <div class="metadata-item">
                        <div class="metadata-label">Versioner</div>
                        <div class="metadata-value">${chapter.versions.length}</div>
                    </div>
                </div>
                ${chapter.synopsis ? `<p style="margin-top: 15px;">${chapter.synopsis}</p>` : ''}
            </div>
        `;
    });

    container.innerHTML = html;
}

// Initialize dashboard when data is loaded
async function initializeDashboard() {
    console.log('🚀 Laddar NOIR Dashboard...');

    // Load data
    const data = await loadDataFromFile();
    window.bookData = data;

    console.log('✅ Data laddad:', data.title);

    // Update title if specified
    if (data.title && data.title !== "Bokprojekt") {
        document.querySelector('h1').textContent = `📚 ${data.title}`;
    }

    // Render all sections
    updateDashboard();
    renderOutline(data.outline);
    renderCharacters(data.characters);
    renderChaptersList(data.chapters);

    console.log('✅ Dashboard initialiserad');
}

// Call initialization when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeDashboard);
} else {
    initializeDashboard();
}
