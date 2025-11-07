/**
 * NOIR Feedback UI Components
 * Interactive forms for providing feedback on outlines and chapters
 */

// ============================================================================
// OUTLINE FEEDBACK MODAL
// ============================================================================

function showOutlineFeedbackModal(projectName, outline) {
    const modal = createModal('Ge Feedback på Outline', `
        <div class="feedback-form">
            <div class="feedback-header">
                <h3>📋 Outline Feedback</h3>
                <p>Granska outlineen och ge din feedback nedan</p>
            </div>

            <div class="outline-preview">
                <div class="outline-section">
                    <h4>Logline</h4>
                    <p>${outline.logline || 'Ej genererad ännu'}</p>
                </div>
                <div class="outline-section">
                    <h4>Hook</h4>
                    <p>${outline.hook || 'Ej genererad ännu'}</p>
                </div>
                <div class="outline-section">
                    <h4>Twist</h4>
                    <p>${outline.twist || 'Ej genererad ännu'}</p>
                </div>
                <div class="outline-section">
                    <h4>Resolution</h4>
                    <p>${outline.resolution || 'Ej genererad ännu'}</p>
                </div>
            </div>

            <div class="feedback-sections">
                <!-- LOGLINE FEEDBACK -->
                <div class="feedback-category">
                    <h4>Logline</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_logline" min="1" max="10" value="7"
                               oninput="document.getElementById('score_logline_value').textContent = this.value">
                        <span id="score_logline_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_logline" rows="3"
                              placeholder="Din feedback på logline..."></textarea>
                    <label>
                        <input type="checkbox" id="change_logline">
                        Föreslå förändring
                    </label>
                </div>

                <!-- HOOK FEEDBACK -->
                <div class="feedback-category">
                    <h4>Hook</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_hook" min="1" max="10" value="7"
                               oninput="document.getElementById('score_hook_value').textContent = this.value">
                        <span id="score_hook_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_hook" rows="3"
                              placeholder="Din feedback på hook..."></textarea>
                    <label>
                        <input type="checkbox" id="change_hook">
                        Föreslå förändring
                    </label>
                </div>

                <!-- TWIST FEEDBACK -->
                <div class="feedback-category">
                    <h4>Twist</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_twist" min="1" max="10" value="7"
                               oninput="document.getElementById('score_twist_value').textContent = this.value">
                        <span id="score_twist_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_twist" rows="3"
                              placeholder="Din feedback på twist..."></textarea>
                    <label>
                        <input type="checkbox" id="change_twist">
                        Föreslå förändring
                    </label>
                </div>

                <!-- RESOLUTION FEEDBACK -->
                <div class="feedback-category">
                    <h4>Resolution</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_resolution" min="1" max="10" value="7"
                               oninput="document.getElementById('score_resolution_value').textContent = this.value">
                        <span id="score_resolution_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_resolution" rows="3"
                              placeholder="Din feedback på resolution..."></textarea>
                    <label>
                        <input type="checkbox" id="change_resolution">
                        Föreslå förändring
                    </label>
                </div>

                <!-- OVERALL FEEDBACK -->
                <div class="feedback-category overall">
                    <h4>Övergripande Feedback</h4>
                    <div class="score-input">
                        <label>Overall Score (1-10):</label>
                        <input type="range" id="score_overall" min="1" max="10" value="7"
                               oninput="document.getElementById('score_overall_value').textContent = this.value">
                        <span id="score_overall_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_overall" rows="4"
                              placeholder="Generella kommentarer och övergripande feedback..."></textarea>
                </div>

                <!-- SPECIFIC REQUESTS -->
                <div class="feedback-category">
                    <h4>Specifika Önskemål till Harper</h4>
                    <textarea id="specific_requests" rows="4"
                              placeholder="Lista specifika ändringar eller förbättringar du vill se (en per rad)..."></textarea>
                </div>
            </div>

            <div class="decision-buttons">
                <button class="btn-decision btn-approve" onclick="submitOutlineFeedback('${projectName}', 'APPROVE')">
                    ✅ Godkänn
                </button>
                <button class="btn-decision btn-revise" onclick="submitOutlineFeedback('${projectName}', 'REVISE')">
                    🔄 Begär Revision
                </button>
                <button class="btn-decision btn-reject" onclick="submitOutlineFeedback('${projectName}', 'REJECT')">
                    ❌ Avslå
                </button>
            </div>

            <div class="decision-help">
                <p><strong>Godkänn:</strong> Outline är bra, gå vidare till Fas 1</p>
                <p><strong>Begär Revision:</strong> Outline behöver förbättras med din feedback</p>
                <p><strong>Avslå:</strong> Outline fungerar inte, börja om från början</p>
            </div>
        </div>
    `);

    document.body.appendChild(modal);
}

async function submitOutlineFeedback(projectName, decision) {
    NOIR.ui.showLoading(true);

    try {
        // Collect all feedback data
        const feedback = {
            decision: decision,
            overallScore: parseInt(document.getElementById('score_overall').value),
            comments: {
                logline: {
                    score: parseInt(document.getElementById('score_logline').value),
                    feedback: document.getElementById('feedback_logline').value,
                    changeRequested: document.getElementById('change_logline').checked
                },
                hook: {
                    score: parseInt(document.getElementById('score_hook').value),
                    feedback: document.getElementById('feedback_hook').value,
                    changeRequested: document.getElementById('change_hook').checked
                },
                twist: {
                    score: parseInt(document.getElementById('score_twist').value),
                    feedback: document.getElementById('feedback_twist').value,
                    changeRequested: document.getElementById('change_twist').checked
                },
                resolution: {
                    score: parseInt(document.getElementById('score_resolution').value),
                    feedback: document.getElementById('feedback_resolution').value,
                    changeRequested: document.getElementById('change_resolution').checked
                }
            },
            overallComments: document.getElementById('feedback_overall').value,
            specificRequests: document.getElementById('specific_requests').value
                .split('\n')
                .filter(line => line.trim())
        };

        // Submit to API
        await NOIR.api.submitOutlineFeedback(projectName, feedback);

        // Close modal
        closeModal();

        // Show success and reload
        NOIR.ui.showLoading(false);
        NOIR.ui.showNotification(`Outline feedback skickad: ${decision}`, 'success');

        // Reload page to show updated status
        setTimeout(() => location.reload(), 1500);

    } catch (error) {
        NOIR.ui.showLoading(false);
        NOIR.ui.showNotification('Fel vid feedback: ' + error.message, 'error');
    }
}

// ============================================================================
// CHAPTER FEEDBACK MODAL
// ============================================================================

function showChapterFeedbackModal(projectName, chapter) {
    const modal = createModal(`Ge Feedback på Kapitel ${chapter.number}`, `
        <div class="feedback-form">
            <div class="feedback-header">
                <h3>📝 Kapitel ${chapter.number} Feedback</h3>
                <p><strong>Titel:</strong> ${chapter.title}</p>
                <p><strong>Version:</strong> ${chapter.currentVersion || 'Draft v1'}</p>
            </div>

            <div class="chapter-preview">
                <h4>Kapiteltext (preview)</h4>
                <div class="text-preview">
                    ${(chapter.text || 'Inte skrivet ännu').substring(0, 500)}...
                </div>
            </div>

            <div class="feedback-sections">
                <!-- PACING -->
                <div class="feedback-category">
                    <h4>⚡ Pacing</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_pacing" min="1" max="10" value="7"
                               oninput="document.getElementById('score_pacing_value').textContent = this.value">
                        <span id="score_pacing_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_pacing" rows="3"
                              placeholder="Hur är tempot? För snabbt/långsamt? Lagom spänning?"></textarea>
                </div>

                <!-- TENSION -->
                <div class="feedback-category">
                    <h4>😰 Tension/Suspense</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_tension" min="1" max="10" value="7"
                               oninput="document.getElementById('score_tension_value').textContent = this.value">
                        <span id="score_tension_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_tension" rows="3"
                              placeholder="Hur är spänningen? Engagerande? Byggande?"></textarea>
                </div>

                <!-- DIALOGUE -->
                <div class="feedback-category">
                    <h4>💬 Dialogue</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_dialogue" min="1" max="10" value="7"
                               oninput="document.getElementById('score_dialogue_value').textContent = this.value">
                        <span id="score_dialogue_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_dialogue" rows="3"
                              placeholder="Låter dialogerna naturliga? Karaktärsdrivna?"></textarea>
                </div>

                <!-- CHARACTER CONSISTENCY -->
                <div class="feedback-category">
                    <h4>🎭 Character Consistency</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_character" min="1" max="10" value="7"
                               oninput="document.getElementById('score_character_value').textContent = this.value">
                        <span id="score_character_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_character" rows="3"
                              placeholder="Agerar karaktärerna konsekvent? Känns deras beslut trovärdiga?"></textarea>
                </div>

                <!-- PROSE QUALITY -->
                <div class="feedback-category">
                    <h4>✍️ Prose Quality</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_prose" min="1" max="10" value="7"
                               oninput="document.getElementById('score_prose_value').textContent = this.value">
                        <span id="score_prose_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_prose" rows="3"
                              placeholder="Hur är språket? Flöde? Läsbarhet?"></textarea>
                </div>

                <!-- PLOT ADVANCEMENT -->
                <div class="feedback-category">
                    <h4>📈 Plot Advancement</h4>
                    <div class="score-input">
                        <label>Score (1-10):</label>
                        <input type="range" id="score_plot" min="1" max="10" value="7"
                               oninput="document.getElementById('score_plot_value').textContent = this.value">
                        <span id="score_plot_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_plot" rows="3"
                              placeholder="Hur mycket driver kapitlet handlingen framåt?"></textarea>
                </div>

                <!-- OVERALL -->
                <div class="feedback-category overall">
                    <h4>Övergripande Feedback</h4>
                    <div class="score-input">
                        <label>Overall Score (1-10):</label>
                        <input type="range" id="score_chapter_overall" min="1" max="10" value="7"
                               oninput="document.getElementById('score_chapter_overall_value').textContent = this.value">
                        <span id="score_chapter_overall_value" class="score-value">7</span>
                    </div>
                    <textarea id="feedback_chapter_overall" rows="4"
                              placeholder="Generella kommentarer..."></textarea>
                </div>

                <!-- MUST FIX -->
                <div class="feedback-category critical">
                    <h4>⚠️ Måste Fixas</h4>
                    <textarea id="must_fix" rows="4"
                              placeholder="Kritiska problem som MÅSTE åtgärdas (en per rad)..."></textarea>
                </div>

                <!-- NICE TO HAVE -->
                <div class="feedback-category">
                    <h4>💡 Nice to Have</h4>
                    <textarea id="nice_to_have" rows="4"
                              placeholder="Förslag på förbättringar (en per rad)..."></textarea>
                </div>
            </div>

            <div class="decision-buttons">
                <button class="btn-decision btn-approve" onclick="submitChapterFeedback('${projectName}', ${chapter.number}, 'APPROVE')">
                    ✅ Godkänn
                </button>
                <button class="btn-decision btn-revise" onclick="submitChapterFeedback('${projectName}', ${chapter.number}, 'REVISE')">
                    🔄 Begär Revision
                </button>
                <button class="btn-decision btn-reject" onclick="submitChapterFeedback('${projectName}', ${chapter.number}, 'REJECT')">
                    ❌ Avslå
                </button>
            </div>

            <div class="decision-help">
                <p><strong>Godkänn:</strong> Kapitlet är klart, gå vidare till nästa</p>
                <p><strong>Begär Revision:</strong> Kapitlet behöver förbättras</p>
                <p><strong>Avslå:</strong> Kapitlet måste skrivas om helt</p>
            </div>
        </div>
    `);

    document.body.appendChild(modal);
}

async function submitChapterFeedback(projectName, chapterNum, decision) {
    NOIR.ui.showLoading(true);

    try {
        const feedback = {
            decision: decision,
            overallScore: parseInt(document.getElementById('score_chapter_overall').value),
            categories: {
                pacing: {
                    score: parseInt(document.getElementById('score_pacing').value),
                    feedback: document.getElementById('feedback_pacing').value
                },
                tension: {
                    score: parseInt(document.getElementById('score_tension').value),
                    feedback: document.getElementById('feedback_tension').value
                },
                dialogue: {
                    score: parseInt(document.getElementById('score_dialogue').value),
                    feedback: document.getElementById('feedback_dialogue').value
                },
                characterConsistency: {
                    score: parseInt(document.getElementById('score_character').value),
                    feedback: document.getElementById('feedback_character').value
                },
                proseQuality: {
                    score: parseInt(document.getElementById('score_prose').value),
                    feedback: document.getElementById('feedback_prose').value
                },
                plotAdvancement: {
                    score: parseInt(document.getElementById('score_plot').value),
                    feedback: document.getElementById('feedback_plot').value
                }
            },
            overallComments: document.getElementById('feedback_chapter_overall').value,
            mustFix: document.getElementById('must_fix').value
                .split('\n')
                .filter(line => line.trim()),
            niceToHave: document.getElementById('nice_to_have').value
                .split('\n')
                .filter(line => line.trim())
        };

        // Submit to API
        await NOIR.api.submitChapterFeedback(projectName, chapterNum, feedback);

        // Close modal
        closeModal();

        // Show success and reload
        NOIR.ui.showLoading(false);
        NOIR.ui.showNotification(`Kapitel ${chapterNum} feedback skickad: ${decision}`, 'success');

        // Reload page
        setTimeout(() => location.reload(), 1500);

    } catch (error) {
        NOIR.ui.showLoading(false);
        NOIR.ui.showNotification('Fel vid feedback: ' + error.message, 'error');
    }
}

// ============================================================================
// MODAL UTILITIES
// ============================================================================

function createModal(title, content) {
    const modal = document.createElement('div');
    modal.className = 'feedback-modal-overlay';
    modal.innerHTML = `
        <div class="feedback-modal">
            <div class="modal-header">
                <h2>${title}</h2>
                <button class="modal-close" onclick="closeModal()">✕</button>
            </div>
            <div class="modal-content">
                ${content}
            </div>
        </div>
    `;
    return modal;
}

function closeModal() {
    const modal = document.querySelector('.feedback-modal-overlay');
    if (modal) {
        modal.remove();
    }
}

// Add modal styles
const modalStyles = document.createElement('style');
modalStyles.textContent = `
    .feedback-modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        overflow-y: auto;
        padding: 20px;
    }

    .feedback-modal {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 12px;
        max-width: 800px;
        width: 100%;
        max-height: 90vh;
        overflow-y: auto;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    }

    .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 25px 30px;
        border-bottom: 2px solid rgba(0, 212, 255, 0.3);
    }

    .modal-header h2 {
        color: #00d4ff;
        margin: 0;
    }

    .modal-close {
        background: none;
        border: none;
        color: #999;
        font-size: 2em;
        cursor: pointer;
        transition: color 0.3s;
    }

    .modal-close:hover {
        color: #ff4444;
    }

    .modal-content {
        padding: 30px;
    }

    .feedback-header {
        margin-bottom: 25px;
    }

    .feedback-header h3 {
        color: #00d4ff;
        margin-bottom: 10px;
    }

    .feedback-header p {
        color: #a0a0a0;
        margin: 5px 0;
    }

    .outline-preview,
    .chapter-preview {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 30px;
    }

    .outline-section {
        margin-bottom: 15px;
    }

    .outline-section h4 {
        color: #60a5fa;
        margin-bottom: 5px;
    }

    .outline-section p,
    .text-preview {
        color: #d0d0d0;
        line-height: 1.6;
    }

    .feedback-sections {
        margin-bottom: 30px;
    }

    .feedback-category {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        border-left: 3px solid #4a5568;
    }

    .feedback-category.overall {
        border-left-color: #00d4ff;
    }

    .feedback-category.critical {
        border-left-color: #ff4444;
    }

    .feedback-category h4 {
        color: #60a5fa;
        margin-bottom: 15px;
    }

    .score-input {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 10px;
    }

    .score-input label {
        color: #b0b0b0;
        white-space: nowrap;
    }

    .score-input input[type="range"] {
        flex: 1;
    }

    .score-value {
        color: #00d4ff;
        font-weight: bold;
        font-size: 1.2em;
        min-width: 30px;
        text-align: center;
    }

    .feedback-category textarea {
        width: 100%;
        padding: 12px;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 6px;
        color: #e0e0e0;
        font-size: 1em;
        resize: vertical;
        font-family: inherit;
    }

    .feedback-category label {
        display: block;
        color: #b0b0b0;
        margin-top: 10px;
        cursor: pointer;
    }

    .feedback-category input[type="checkbox"] {
        margin-right: 8px;
    }

    .decision-buttons {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }

    .btn-decision {
        flex: 1;
        min-width: 150px;
        padding: 15px 25px;
        font-size: 1.1em;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .btn-approve {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
    }

    .btn-approve:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(46, 204, 113, 0.4);
    }

    .btn-revise {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        color: white;
    }

    .btn-revise:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(243, 156, 18, 0.4);
    }

    .btn-reject {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
    }

    .btn-reject:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(231, 76, 60, 0.4);
    }

    .decision-help {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 6px;
        font-size: 0.9em;
    }

    .decision-help p {
        margin: 5px 0;
        color: #a0a0a0;
    }

    .decision-help strong {
        color: #00d4ff;
    }
`;
document.head.appendChild(modalStyles);

// Export functions
window.FeedbackUI = {
    showOutlineFeedbackModal,
    showChapterFeedbackModal,
    submitOutlineFeedback,
    submitChapterFeedback
};
