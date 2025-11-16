// script.js - Gestor de Tarefas com Sincronização em Tempo Real (multi-aba)

const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');
const statsEl = document.getElementById('stats');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// === RENDERIZAÇÃO ===
function renderTasks() {
  taskList.innerHTML = '';
  tasks.forEach((task, index) => {
    const li = document.createElement('li');
    li.className = `task-item ${task.completed ? 'completed' : ''}`;
    li.innerHTML = `
      <input type="checkbox" ${task.completed ? 'checked' : ''} data-index="${index}">
      <span class="task-text">${escapeHTML(task.text)}</span>
      <button class="delete-btn" data-index="${index}">×</button>
    `;
    taskList.appendChild(li);
  });
  updateStats();
}

// === ESTATÍSTICAS ===
function updateStats() {
  const total = tasks.length;
  const completed = tasks.filter(t => t.completed).length;
  statsEl.textContent = `${total} tarefa${total !== 1 ? 's' : ''} | ${completed} concluída${completed !== 1 ? 's' : ''}`;
}

// === ADICIONAR TAREFA ===
function addTask(text) {
  try {
    const trimmed = text.trim();
    if (!trimmed) throw new Error("A tarefa não pode estar vazia.");

    tasks.push({ text: trimmed, completed: false });
    saveAndRender();
    taskInput.value = '';
    taskInput.focus();
  } catch (error) {
    showError(error.message);
  }
}

// === TOGGLE CONCLUSÃO ===
function toggleTask(index) {
  try {
    if (tasks[index] === undefined) throw new Error("Tarefa não encontrada.");
    tasks[index].completed = !tasks[index].completed;
    saveAndRender();
  } catch (error) {
    console.error(error);
  }
}

// === REMOVER TAREFA ===
function deleteTask(index) {
  try {
    if (!confirm("Remover esta tarefa?")) return;
    tasks.splice(index, 1);
    saveAndRender();
  } catch (error) {
    console.error(error);
  }
}

// === SALVAR E SINCRONIZAR ===
function saveAndRender() {
  localStorage.setItem('tasks', JSON.stringify(tasks));
  renderTasks();
}

// === ESCAPAR HTML (segurança) ===
function escapeHTML(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

// === MOSTRAR ERRO TEMPORÁRIO ===
function showError(message) {
  const errorEl = document.createElement('div');
  errorEl.className = 'error-toast';
  errorEl.textContent = message;
  document.body.appendChild(errorEl);
  setTimeout(() => errorEl.remove(), 3000);
}

// === EVENTOS LOCAIS ===
taskForm.addEventListener('submit', (e) => {
  e.preventDefault();
  addTask(taskInput.value);
});

taskList.addEventListener('change', (e) => {
  if (e.target.type === 'checkbox') {
    const index = parseInt(e.target.dataset.index);
    toggleTask(index);
  }
});

taskList.addEventListener('click', (e) => {
  if (e.target.classList.contains('delete-btn')) {
    const index = parseInt(e.target.dataset.index);
    deleteTask(index);
  }
});

// === TEMPO REAL ENTRE ABAS ===
// Escuta mudanças no localStorage feitas por OUTRAS abas
window.addEventListener('storage', (e) => {
  if (e.key === 'tasks') {
    tasks = JSON.parse(e.newValue) || [];
    renderTasks();
  }
});

// === INICIALIZAÇÃO ===
renderTasks();

// Foco automático no input ao carregar
taskInput.focus();