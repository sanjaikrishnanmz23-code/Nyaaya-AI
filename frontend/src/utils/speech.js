/**
 * Web Speech API Utilities
 * Bilingual Text-to-Speech and Speech Recognition (English & Tamil).
 */

export function speakText(text, lang = 'en', onEnd = () => {}) {
  if (!('speechSynthesis' in window)) {
    console.warn('Speech synthesis not supported on this browser.');
    return false;
  }

  // Cancel any ongoing speech
  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  
  if (lang === 'ta') {
    utterance.lang = 'ta-IN';
  } else {
    utterance.lang = 'en-IN';
  }

  utterance.rate = 0.95;
  utterance.pitch = 1.0;

  // Attempt to select an authentic native voice if available
  const voices = window.speechSynthesis.getVoices();
  const targetVoice = voices.find(v => {
    if (lang === 'ta') return v.lang.startsWith('ta');
    return v.lang.startsWith('en-IN') || v.lang.startsWith('en');
  });

  if (targetVoice) {
    utterance.voice = targetVoice;
  }

  utterance.onend = onEnd;
  utterance.onerror = (e) => {
    console.warn('Speech synthesis error:', e);
    onEnd();
  };

  window.speechSynthesis.speak(utterance);
  return true;
}

export function stopSpeaking() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
}

export function createSpeechRecognizer(lang = 'en', onResult, onError, onEnd) {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    return null;
  }

  const recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = lang === 'ta' ? 'ta-IN' : 'en-IN';

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    if (onResult) onResult(transcript);
  };

  recognition.onerror = (event) => {
    if (onError) onError(event.error);
  };

  recognition.onend = () => {
    if (onEnd) onEnd();
  };

  return recognition;
}
