import React, { useState } from 'react';
import { Scale, Search, Menu, X, MessageSquare, Compass, Landmark, HelpCircle, PhoneCall, LayoutDashboard } from 'lucide-react';
import LanguageSelector from './LanguageSelector';

export default function Navbar({ activePage, setActivePage, currentLang, setCurrentLang, onOpenSearch }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navLinks = [
    { id: 'home', label: 'Home', labelTa: 'முகப்பு', icon: Scale },
    { id: 'chat', label: 'Ask AI', labelTa: 'AI கேள்வி', icon: MessageSquare, highlight: true },
    { id: 'rights', label: 'Explore Rights', labelTa: 'உரிமைகள்', icon: Compass },
    { id: 'services', label: 'Gov Services', labelTa: 'அரசு சேவைகள்', icon: Landmark },
    { id: 'actions', label: 'What Should I Do?', labelTa: 'வழிகாட்டி', icon: HelpCircle },
    { id: 'emergency', label: 'Emergency', labelTa: 'அவசர உதவி', icon: PhoneCall },
    { id: 'dashboard', label: 'Dashboard', labelTa: 'வரலாறு', icon: LayoutDashboard },
  ];

  const handleNav = (id) => {
    setActivePage(id);
    setMobileMenuOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <header className="sticky top-0 z-40 w-full glass-panel border-b border-cyan-500/10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-18 flex items-center justify-between gap-4">
        {/* Logo / Brand */}
        <div
          onClick={() => handleNav('home')}
          className="flex items-center gap-3 cursor-pointer group select-none"
        >
          <div className="relative p-2 rounded-xl bg-gradient-to-tr from-cyan-500/20 via-blue-500/20 to-purple-600/20 border border-cyan-400/30 group-hover:border-cyan-400 transition-all shadow-glow-cyan">
            <Scale className="w-5 h-5 sm:w-6 sm:h-6 text-brand-cyan group-hover:scale-110 transition-transform" />
            <div className="absolute -bottom-1 -right-1 w-2 h-2 rounded-full bg-cyan-400 animate-ping" />
          </div>
          <div className="flex flex-col text-left">
            <div className="flex items-center gap-1.5">
              <span className="text-lg sm:text-xl font-black tracking-tight text-white font-sans">
                Nyaaya<span className="text-brand-cyan">AI</span>
              </span>
              <span className="px-1.5 py-0.5 rounded text-[10px] font-mono uppercase bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">
                Civic
              </span>
            </div>
            <span className="text-[10px] text-slate-400 tracking-wide hidden sm:inline">
              Citizen Rights Assistant • குடிமக்கள் உரிமைகள்
            </span>
          </div>
        </div>

        {/* Desktop Nav Links */}
        <nav className="hidden lg:flex items-center gap-1">
          {navLinks.map((link) => {
            const Icon = link.icon;
            const isActive = activePage === link.id;
            return (
              <button
                key={link.id}
                onClick={() => handleNav(link.id)}
                className={`px-3 py-1.5 rounded-xl text-xs font-medium transition-all flex items-center gap-1.5 ${
                  isActive
                    ? 'bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 shadow-sm'
                    : 'text-slate-300 hover:text-white hover:bg-slate-800/50'
                }`}
              >
                <Icon className={`w-3.5 h-3.5 ${isActive ? 'text-brand-cyan' : 'text-slate-400'}`} />
                <span>{link.label}</span>
                {currentLang === 'ta' && (
                  <span className="text-[10px] opacity-75 font-tamil">({link.labelTa})</span>
                )}
              </button>
            );
          })}
        </nav>

        {/* Right Action Cluster */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* Quick Search trigger button */}
          <button
            onClick={onOpenSearch}
            className="flex items-center gap-2 px-2.5 sm:px-3 py-1.5 rounded-xl bg-slate-900/80 hover:bg-slate-800 border border-slate-700/60 text-slate-300 hover:text-white text-xs transition-colors shadow-inner"
            title="Search anything (Ctrl+K)"
          >
            <Search className="w-3.5 h-3.5 text-brand-cyan" />
            <span className="hidden md:inline text-slate-400">Search</span>
            <kbd className="hidden md:inline px-1.5 py-0.2 rounded bg-slate-800 border border-slate-700 text-[10px] font-mono text-slate-400">
              Ctrl+K
            </kbd>
          </button>

          {/* Language Selector */}
          <LanguageSelector
            currentLang={currentLang}
            onChange={setCurrentLang}
            compact={true}
          />

          {/* CTA Ask AI Button */}
          <button
            onClick={() => handleNav('chat')}
            className="hidden sm:flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-semibold text-xs transition-all shadow-glow-cyan hover:scale-[1.02]"
          >
            <MessageSquare className="w-3.5 h-3.5" />
            <span>Ask NyaayaAI</span>
          </button>

          {/* Mobile Menu Toggle */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="lg:hidden p-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white"
            aria-label="Toggle menu"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Menu Dropdown */}
      {mobileMenuOpen && (
        <div className="lg:hidden glass-panel border-b border-cyan-500/20 px-4 pt-3 pb-6 space-y-2 animate-fadeIn">
          {navLinks.map((link) => {
            const Icon = link.icon;
            const isActive = activePage === link.id;
            return (
              <button
                key={link.id}
                onClick={() => handleNav(link.id)}
                className={`w-full px-3.5 py-2.5 rounded-xl text-left text-sm font-medium flex items-center justify-between ${
                  isActive
                    ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30'
                    : 'text-slate-200 hover:bg-slate-800/60'
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon className={`w-4 h-4 ${isActive ? 'text-brand-cyan' : 'text-slate-400'}`} />
                  <span>{link.label}</span>
                </div>
                <span className="text-xs text-cyan-300/80 font-tamil">{link.labelTa}</span>
              </button>
            );
          })}

          <div className="pt-2 border-t border-slate-800">
            <button
              onClick={() => handleNav('chat')}
              className="w-full py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-bold text-sm flex items-center justify-center gap-2 shadow-glow-cyan"
            >
              <MessageSquare className="w-4 h-4" />
              <span>Ask NyaayaAI Assistant</span>
            </button>
          </div>
        </div>
      )}
    </header>
  );
}
