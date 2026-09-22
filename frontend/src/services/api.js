/**
 * NyaayaAI API Client
 * Connects React frontend to FastAPI backend.
 */

const API_BASE = '/api';

export async function askQuestion(question, language = 'both', sessionId = 'default-session') {
  const response = await fetch(`${API_BASE}/chat/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, language, session_id: sessionId })
  });
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Failed to get answer from NyaayaAI');
  }
  return response.json();
}

export async function fetchCategories() {
  const response = await fetch(`${API_BASE}/rights/categories`);
  if (!response.ok) throw new Error('Failed to load rights categories');
  return response.json();
}

export async function fetchCategory(id) {
  const response = await fetch(`${API_BASE}/rights/${id}`);
  if (!response.ok) throw new Error('Failed to load category details');
  return response.json();
}

export async function fetchServices(category = 'all', q = '') {
  const params = new URLSearchParams();
  if (category && category !== 'all') params.append('category', category);
  if (q) params.append('q', q);
  const response = await fetch(`${API_BASE}/services/?${params.toString()}`);
  if (!response.ok) throw new Error('Failed to load government services');
  return response.json();
}

export async function fetchProblems() {
  const response = await fetch(`${API_BASE}/actions/problems`);
  if (!response.ok) throw new Error('Failed to load guided problem workflows');
  return response.json();
}

export async function fetchEmergencyContacts() {
  const response = await fetch(`${API_BASE}/emergency/contacts`);
  if (!response.ok) throw new Error('Failed to load emergency contacts');
  return response.json();
}

export async function fetchHistory() {
  const response = await fetch(`${API_BASE}/history/`);
  if (!response.ok) throw new Error('Failed to load recent history');
  return response.json();
}

export async function clearHistoryApi() {
  const response = await fetch(`${API_BASE}/history/clear`, { method: 'DELETE' });
  if (!response.ok) throw new Error('Failed to clear history');
  return response.json();
}

export async function globalSearch(q) {
  if (!q || !q.trim()) return { results: { rights: [], services: [], actions: [] }, total: 0 };
  const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(q.trim())}`);
  if (!response.ok) throw new Error('Search failed');
  return response.json();
}
