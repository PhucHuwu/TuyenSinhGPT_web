// Hàm định dạng số
function formatNumber(num) {
    return num.toFixed(2);
}

// Hàm rút gọn chuỗi
function truncateString(str, maxLength) {
    if (str && str.length > maxLength) {
        return str.substring(0, maxLength) + '...';
    }
    return str;
}

// Hàm chuyển đổi màu dựa trên điểm
function getScoreColor(score) {
    if (score >= 28) return 'text-danger fw-bold';
    if (score >= 25) return 'text-warning fw-bold';
    if (score >= 22) return 'text-success fw-bold';
    return 'text-primary';
}

// Hàm tạo thông báo
function showToast(message, type = 'success') {
    const toastContainer = document.createElement('div');
    toastContainer.className = 'position-fixed bottom-0 end-0 p-3';
    toastContainer.style.zIndex = '5';
    
    const toastHtml = `
    <div class="toast show" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header bg-${type} text-white">
            <strong class="me-auto">Thông báo</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            ${message}
        </div>
    </div>
    `;
    
    toastContainer.innerHTML = toastHtml;
    document.body.appendChild(toastContainer);
    
    setTimeout(() => {
        toastContainer.remove();
    }, 3000);
}