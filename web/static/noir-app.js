/**
 * NOIR Interactive Frontend
 * JavaScript för interaktiv kommunikation med backend
 */

const API_BASE = 'http://localhost:5000/api';

// ============================================================================
// API HELPERS
// ============================================================================

async function apiCall(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        },
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || 'API request failed');
        }

        return result;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// ============================================================================
// PROJECT MANAGEMENT
// ============================================================================

async function listProjects() {
    return await apiCall('/projects');
}

async function getProject(projectName) {
    return await apiCall(`/projects/${projectName}`);
}

async function createProject(projectName, data) {
    return await apiCall(`/projects/${projectName}`, 'POST', data);
}

// ============================================================================
// PLOT INTAKE
// ============================================================================

async function submitPlotIntake(projectName, plotData) {
    return await apiCall(`/projects/${projectName}/plot-intake`, 'POST', plotData);
}

// ============================================================================
// OUTLINE FEEDBACK
// ============================================================================

async function getOutline(projectName) {
    return await apiCall(`/projects/${projectName}/outline`);
}

async function submitOutlineFeedback(projectName, feedback) {
    return await apiCall(`/projects/${projectName}/outline/feedback`, 'POST', feedback);
}

// ============================================================================
// CHARACTERS
// ============================================================================

async function getCharacters(projectName) {
    return await apiCall(`/projects/${projectName}/characters`);
}

async function submitCharactersFeedback(projectName, feedback) {
    return await apiCall(`/projects/${projectName}/characters/feedback`, 'POST', feedback);
}

// ============================================================================
// CHAPTERS
// ============================================================================

async function getChapters(projectName) {
    return await apiCall(`/projects/${projectName}/chapters`);
}

async function getChapter(projectName, chapterNum) {
    return await apiCall(`/projects/${projectName}/chapters/${chapterNum}`);
}

async function submitChapterFeedback(projectName, chapterNum, feedback) {
    return await apiCall(`/projects/${projectName}/chapters/${chapterNum}/feedback`, 'POST', feedback);
}

// ============================================================================
// UI HELPERS
// ============================================================================

function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        background: ${type === 'success' ? '#2ecc71' : type === 'error' ? '#e74c3c' : '#f39c12'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

function showLoading(show = true) {
    let loader = document.getElementById('global-loader');

    if (show) {
        if (!loader) {
            loader = document.createElement('div');
            loader.id = 'global-loader';
            loader.innerHTML = '<div class="spinner"></div>';
            loader.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.7);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
            `;
            document.body.appendChild(loader);
        }
        loader.style.display = 'flex';
    } else {
        if (loader) {
            loader.style.display = 'none';
        }
    }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(400px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(400px); opacity: 0; }
    }

    .spinner {
        border: 4px solid rgba(255,255,255,0.3);
        border-top: 4px solid white;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
`;
document.head.appendChild(style);

// Export for use in other scripts
window.NOIR = {
    api: {
        listProjects,
        getProject,
        createProject,
        submitPlotIntake,
        getOutline,
        submitOutlineFeedback,
        getCharacters,
        submitCharactersFeedback,
        getChapters,
        getChapter,
        submitChapterFeedback
    },
    ui: {
        showNotification,
        showLoading
    }
};
