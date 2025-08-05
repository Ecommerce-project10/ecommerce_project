// File upload preview functionality
(function() {
    // DOM elements
    const imageInput = document.getElementById('image');
    const uploadArea = document.querySelector('.upload-area');
    
    // Upload prompt HTML
    const uploadPromptHTML = `
        <i class="fas fa-cloud-upload-alt"></i>
        <h5>Click to upload image</h5>
        <p class="mb-0 text-muted">JPG, PNG, WEBP, SVG up to 10MB</p>
    `;
    
    // Initialize upload area
    function initializeUploadArea() {
        uploadArea.innerHTML = uploadPromptHTML;
        uploadArea.addEventListener('click', triggerFileInput);
    }
    
    // Trigger file input click
    function triggerFileInput() {
        imageInput.click();
    }
    
    // Handle file selection
    function handleFileSelection(event) {
        const file = event.target.files[0];
        
        if (file) {
            displayImagePreview(file);
        } else {
            resetUploadArea();
        }
    }
    
    // Display image preview
    function displayImagePreview(file) {
        const reader = new FileReader();
        
        reader.onload = function(event) {
            const previewHTML = createPreviewHTML(event.target.result, file.name);
            uploadArea.innerHTML = previewHTML;
            setupRemoveButton();
        };
        
        reader.readAsDataURL(file);
    }
    
    // Create preview HTML
    function createPreviewHTML(imageSrc, fileName) {
        return `
            <div style="position: relative; display: inline-block;">
                <img src="${imageSrc}" style="max-width: 100%; max-height: 200px; border-radius: 8px;" alt="Preview">
                <button type="button" class="btn-close" style="position: absolute; top: 5px; right: 5px; background-color: red !important;padding: 5px;" id="removeImageBtn" aria-label="Remove image"></button>
            </div>
            <p class="mt-2 mb-0"><strong>${fileName}</strong></p>
            <small class="text-muted">Click to change image</small>
        `;
    }
    
    // Setup remove button functionality
    function setupRemoveButton() {
        const removeButton = document.getElementById('removeImageBtn');
        
        if (removeButton) {
            removeButton.addEventListener('click', function(event) {
                event.stopPropagation();
                resetUploadArea();
            });
        }
    }
    
    // Reset upload area to initial state
    function resetUploadArea() {
        uploadArea.innerHTML = uploadPromptHTML;
        imageInput.value = '';
    }
    
    // Initialize when DOM is fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        initializeUploadArea();
        imageInput.addEventListener('change', handleFileSelection);
    });
})();

// Form validation animations
(function() {
    function setupInputAnimations() {
        const formInputs = document.querySelectorAll('.form-control, .form-select');
        
        formInputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.style.transform = 'scale(1.02)';
            });
            
            input.addEventListener('blur', function() {
                this.parentElement.style.transform = 'scale(1)';
            });
        });
    }
    
    // Initialize when DOM is fully loaded
    document.addEventListener('DOMContentLoaded', setupInputAnimations);
})();