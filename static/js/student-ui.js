// student-ui.js - Sidebar toggle and CSRF helper

document.addEventListener('DOMContentLoaded', function() {
  const sidebarToggle = document.getElementById('sidebarToggle');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');

  if (sidebarToggle && sidebar && overlay) {
    sidebarToggle.addEventListener('click', function() {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('hidden');
    });

    overlay.addEventListener('click', function() {
      sidebar.classList.remove('open');
      overlay.classList.add('hidden');
    });
  }
});

// CSRF token helper for AJAX
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

const csrftoken = getCookie('csrftoken');

// Add CSRF token to AJAX requests
function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

document.addEventListener('DOMContentLoaded', function() {
  const originalFetch = window.fetch;
  window.fetch = function(...args) {
    let [resource, config] = args;
    config = config || {};
    if (!csrfSafeMethod(config.method) && !config.headers?.['X-CSRFToken']) {
      config.headers = config.headers || {};
      config.headers['X-CSRFToken'] = csrftoken;
    }
    return originalFetch(resource, config);
  };
});
