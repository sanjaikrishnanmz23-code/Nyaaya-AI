import React from 'react';
import { Languages } from 'lucide-react';

export default function LanguageSelector({ currentLang, onChange, compact = false }) {
  const options = [
    { id: 'en', label: 'English', sub: 'English' },
    { id: 'ta', label: 'தமிழ்', sub: 'Tamil' },
    { id: 'both', label: 'Both', sub: 'இரண்டும்' },
  ];

  return (
    <div className={`inline-flex items-center p-1 rounded-xl bg-navy-900/90 border border-slate-700/60 backdrop-blur-md ${compact ? 'text-xs' : 'text-sm'}`}>
      <div className="flex items-center gap-1.5 px-2 text-slate-400">
        <Languages className="w-3.5 h-3.5 text-brand-cyan" />
      </div>
      <div className="flex items-center gap-1">
        {options.map((opt) => {
          const isActive = currentLang === opt.id;
          return (
            <button
              key={opt.id}
              onClick={() => onChange(opt.id)}
              className={`px-3 py-1 rounded-lg font-medium transition-all duration-200 flex items-center gap-1.5 ${
                isActive
                  ? 'bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-sm shadow-cyan-500/30'
                  : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <span>{opt.label}</span>
              {opt.id === 'both' && (
                <span className="text-[10px] opacity-80 font-tamil hidden sm:inline">({opt.sub})</span>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
