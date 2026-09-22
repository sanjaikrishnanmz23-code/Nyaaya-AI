import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import ParticleField from './components/ParticleField';
import GlobalSearchModal from './components/GlobalSearchModal';

// Pages
import LandingPage from './pages/LandingPage';
import ChatPage from './pages/ChatPage';
import RightsExplorer from './pages/RightsExplorer';
import ServicesDirectory from './pages/ServicesDirectory';
import ActionGuidePage from './pages/ActionGuidePage';
import EmergencyPage from './pages/EmergencyPage';
import DashboardPage from './pages/DashboardPage';

export default function App() {
  const [activePage, setActivePage] = useState('home');
  const [currentLang, setCurrentLang] = useState(() => {
    return localStorage.getItem('nyaaya_lang') || 'both';
  });
  const [initialPrompt, setInitialPrompt] = useState('');
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [selectedCatId, setSelectedCatId] = useState(null);
  const [selectedServiceId, setSelectedServiceId] = useState(null);
  const [selectedProblemId, setSelectedProblemId] = useState(null);

  // LocalStorage Bookmarks
  const [savedBookmarks, setSavedBookmarks] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem('nyaaya_bookmarks') || '[]');
    } catch {
      return [];
    }
  });

  // Save language preference
  const handleLanguageChange = (lang) => {
    setCurrentLang(lang);
    localStorage.setItem('nyaaya_lang', lang);
  };

  // Keyboard shortcut Ctrl+K / Cmd+K for global search
  useEffect(() => {
    const handleKeyDown = (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        setIsSearchOpen((prev) => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Save bookmark handler
  const handleSaveBookmark = (bookmarkItem) => {
    setSavedBookmarks((prev) => {
      const exists = prev.some((b) => b.item_id === bookmarkItem.item_id);
      let updated;
      if (exists) {
        updated = prev.filter((b) => b.item_id !== bookmarkItem.item_id);
      } else {
        updated = [bookmarkItem, ...prev];
      }
      localStorage.setItem('nyaaya_bookmarks', JSON.stringify(updated));
      return updated;
    });
  };

  const handleClearBookmarks = () => {
    setSavedBookmarks([]);
    localStorage.removeItem('nyaaya_bookmarks');
  };

  // Direct prompt launch from landing page
  const handleAskPrompt = (promptText) => {
    setInitialPrompt(promptText);
    setActivePage('chat');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Selection from global search modal
  const handleSelectSearchResult = (type, id) => {
    if (type === 'right') {
      setSelectedCatId(id);
      setActivePage('rights');
    } else if (type === 'service') {
      setSelectedServiceId(id);
      setActivePage('services');
    } else if (type === 'action') {
      setSelectedProblemId(id);
      setActivePage('actions');
    }
  };

  return (
    <div className="relative min-h-screen flex flex-col bg-navy-950 text-slate-100 selection:bg-brand-cyan/20 selection:text-brand-cyan">
      {/* Dynamic Canvas Particle Mesh Background */}
      <ParticleField />

      {/* Sticky Glass Navbar */}
      <Navbar
        activePage={activePage}
        setActivePage={setActivePage}
        currentLang={currentLang}
        setCurrentLang={handleLanguageChange}
        onOpenSearch={() => setIsSearchOpen(true)}
      />

      {/* Global Search Modal (Ctrl+K) */}
      <GlobalSearchModal
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        onSelectResult={handleSelectSearchResult}
      />

      {/* Main View Area */}
      <main className="flex-1 relative z-10">
        {activePage === 'home' && (
          <LandingPage
            onNavigate={(page) => {
              setActivePage(page);
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
            onAskPrompt={handleAskPrompt}
            currentLang={currentLang}
          />
        )}

        {activePage === 'chat' && (
          <ChatPage
            initialPrompt={initialPrompt}
            currentLang={currentLang}
            setCurrentLang={handleLanguageChange}
            onSaveBookmark={handleSaveBookmark}
            savedBookmarks={savedBookmarks}
          />
        )}

        {activePage === 'rights' && (
          <RightsExplorer
            onAskQuestion={handleAskPrompt}
            selectedCatId={selectedCatId}
          />
        )}

        {activePage === 'services' && (
          <ServicesDirectory
            selectedServiceId={selectedServiceId}
          />
        )}

        {activePage === 'actions' && (
          <ActionGuidePage
            selectedProblemId={selectedProblemId}
          />
        )}

        {activePage === 'emergency' && (
          <EmergencyPage />
        )}

        {activePage === 'dashboard' && (
          <DashboardPage
            currentLang={currentLang}
            setCurrentLang={handleLanguageChange}
            savedBookmarks={savedBookmarks}
            onClearBookmarks={handleClearBookmarks}
            onAskQuestion={handleAskPrompt}
          />
        )}
      </main>

      {/* Footer */}
      <Footer
        onNavigate={(page) => {
          setActivePage(page);
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }}
      />
    </div>
  );
}
