// goals.js
document.addEventListener('DOMContentLoaded', function() {
    // Variablen für DOM-Elemente
    const goalsContainer = document.getElementById('goals-container');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const updateModal = document.getElementById('update-modal');
    const closeModalBtn = document.querySelector('.close');
    const updateForm = document.getElementById('update-form');
    const goalIdInput = document.getElementById('goal-id');
    const currentProgressInput = document.getElementById('current-progress');
    const unitDisplay = document.getElementById('unit-display');
    
    // Filter-Funktionalität
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Aktiven Button markieren
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            const goalCards = document.querySelectorAll('.goal-card');
            
            goalCards.forEach(card => {
                if (filter === 'all' || card.getAttribute('data-category') === filter) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
    
    // Berechnung der verbleibenden Tage für jedes Ziel
    document.querySelectorAll('.time-remaining').forEach(timeElement => {
        const endDate = new Date(timeElement.getAttribute('data-end'));
        const today = new Date();
        const timeDiff = endDate - today;
        const daysLeft = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
        
        const daysElement = timeElement.querySelector('.days-left');
        daysElement.textContent = daysLeft > 0 ? daysLeft : 0;
        
        // Hervorheben, wenn weniger als 7 Tage verbleiben
        if (daysLeft <= 7 && daysLeft > 0) {
            timeElement.style.color = '#e74c3c';
        } else if (daysLeft <= 0) {
            timeElement.textContent = 'Frist abgelaufen!';
            timeElement.style.color = '#e74c3c';
            timeElement.style.fontWeight = 'bold';
        }
    });
    
    // Event-Listener für "Fortschritt aktualisieren" Buttons
    document.querySelectorAll('.update-btn').forEach(button => {
        button.addEventListener('click', function() {
            const goalId = this.getAttribute('data-id');
            const goalCard = this.closest('.goal-card');
            
            // Extrahiere Einheit und aktuellen Fortschritt
            const progressText = goalCard.querySelector('.progress-info span').textContent;
            const currentProgress = progressText.match(/Fortschritt: (\d+) von \d+ (.+)/);
            
            if (currentProgress) {
                const progressValue = currentProgress[1];
                const unit = currentProgress[2];
                
                // Befülle das Modal mit den aktuellen Werten
                goalIdInput.value = goalId;
                currentProgressInput.value = progressValue;
                unitDisplay.textContent = unit;
                
                // Zeige das Modal an
                updateModal.style.display = 'block';
            }
        });
    });
    
    // Schließen des Modals
    closeModalBtn.addEventListener('click', function() {
        updateModal.style.display = 'none';
    });
    
    // Klick außerhalb des Modals schließt es
    window.addEventListener('click', function(event) {
        if (event.target === updateModal) {
            updateModal.style.display = 'none';
        }
    });
    
    // Fortschritt aktualisieren (AJAX-Request)
    updateForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const goalId = goalIdInput.value;
        const newProgress = currentProgressInput.value;
        
        // CSRF-Token aus dem Cookie extrahieren (für Django)
        const csrftoken = getCookie('csrftoken');
        
        // AJAX-Request an den Server
        fetch('/update-goal-progress/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                goal_id: goalId,
                progress: newProgress
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Erfolgreiche Aktualisierung
                updateModal.style.display = 'none';
                // Seite neu laden, um die Änderungen anzuzeigen
                window.location.reload();
            } else {
                alert('Fehler beim Aktualisieren des Fortschritts: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Fehler:', error);
            alert('Ein Fehler ist aufgetreten. Bitte versuche es später erneut.');
        });
    });
    
    // Hilfsfunktion zum Extrahieren des CSRF-Tokens aus Cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Edit-Button Funktionalität 
    // (Hier nur ein Platzhalter - in einer echten Implementation würde dies zu einer Edit-Seite führen)
    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', function() {
            const goalId = this.getAttribute('data-id');
            window.location.href = `/edit-goal/${goalId}/`;
        });
    });
});