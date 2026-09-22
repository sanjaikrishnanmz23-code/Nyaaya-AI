import React, { useState, useEffect, useRef } from 'react';
import { Search, X, Scale, Landmark, ShieldAlert, ArrowRight, Loader2 } from 'lucide-react';
import { globalSearch } from '../services/api';

export default function GlobalSearchModal({ isOpen, onClose, onSelectResult }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState({ rights: [], services: [], actions: [] });
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);
  const inputRef = useRef(null);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 50);
    } else {
      setQuery('');
      setResults({ rights: [], services: [], actions: [] });
      setTotal(0);
    }
  }, [isOpen]);

  useEffect(() => {
    if (!query.trim()) {
      setResults({ rights: [], services: [], actions: [] });
      setTotal(0);
      return;
    }

    const timer = setTimeout(async () => {
      setLoading(true);
      try {
        const data = await globalSearch(query);
        setResults(data.results || { rights: [], services: [], actions: [] });
        setTotal(data.total || 0);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }, 250);

    return () => clearTimeout(timer);
  }, [query]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-16 sm:pt-24 px-4 bg-black/75 backdrop-blur-md">
      <div className="relative w-full max-w-2xl bg-navy-900 border border-cyan-500/30 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[80vh] text-left">
        {/* Search Input Bar */}
        <div className="relative flex items-center px-4 py-3.5 border-b border-slate-800 bg-slate-950/60">
          <Search className="w-5 h-5 text-brand-cyan shrink-0 mr-3" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search rights, services, problem guides, or keywords (e.g. salary, police, aadhaar)..."
            className="w-full bg-transparent text-slate-100 placeholder-slate-500 text-sm focus:outline-none"
          />
          {loading && <Loader2 className="w-4 h-4 text-cyan-400 animate-spin mr-2" />}
          {query && (
            <button onClick={() => setQuery('')} className="p-1 text-slate-400 hover:text-white mr-1">
              <X className="w-4 h-4" />
            </button>
          )}
          <button
            onClick={onClose}
            className="px-2 py-0.5 text-xs text-slate-400 hover:text-white border border-slate-700 rounded bg-slate-800"
          >
            ESC
          </button>
        </div>

        {/* Results Body */}
        <div className="p-4 overflow-y-auto space-y-4">
          {!query.trim() && (
            <div className="py-8 text-center text-slate-400 space-y-2">
              <p className="text-sm font-medium">Quick search across the entire Indian Citizen Rights platform.</p>
              <div className="flex flex-wrap items-center justify-center gap-2 pt-2">
                {['Salary Withheld', 'Aadhaar Update', 'Police Encounter', 'Consumer Court', 'RTI Online'].map((tag) => (
                  <button
                    key={tag}
                    onClick={() => setQuery(tag)}
                    className="px-2.5 py-1 rounded-full text-xs bg-slate-800/80 border border-slate-700/60 text-slate-300 hover:border-cyan-400"
                  >
                    {tag}
                  </button>
                ))}
              </div>
            </div>
          )}

          {query.trim() && total === 0 && !loading && (
            <div className="py-8 text-center text-slate-400">
              <p className="text-sm">No direct statutory matches found for "{query}".</p>
              <p className="text-xs text-slate-500 mt-1">Try searching with broader terms or ask NyaayaAI directly in chat.</p>
            </div>
          )}

          {/* Rights Matches */}
          {results.rights && results.rights.length > 0 && (
            <div className="space-y-2">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-cyan-300 uppercase tracking-wider">
                <Scale className="w-3.5 h-3.5" />
                <span>Citizen Rights ({results.rights.length})</span>
              </div>
              <div className="space-y-1.5">
                {results.rights.map((item) => (
                  <div
                    key={item.id}
                    onClick={() => {
                      onSelectResult('right', item.id);
                      onClose();
                    }}
                    className="p-2.5 rounded-xl bg-slate-950/60 hover:bg-slate-800/60 border border-slate-800 hover:border-cyan-500/30 cursor-pointer flex items-center justify-between group transition-all"
                  >
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="text-sm font-semibold text-slate-100 group-hover:text-cyan-300">{item.title}</span>
                        <span className="text-xs text-cyan-400 font-tamil">({item.title_tamil})</span>
                      </div>
                      <p className="text-xs text-slate-400 line-clamp-1 mt-0.5">{item.desc}</p>
                    </div>
                    <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-cyan-400 transition-transform group-hover:translate-x-1 shrink-0 ml-2" />
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Government Services Matches */}
          {results.services && results.services.length > 0 && (
            <div className="space-y-2">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-blue-400 uppercase tracking-wider">
                <Landmark className="w-3.5 h-3.5" />
                <span>Government Services ({results.services.length})</span>
              </div>
              <div className="space-y-1.5">
                {results.services.map((item) => (
                  <div
                    key={item.id}
                    onClick={() => {
                      onSelectResult('service', item.id);
                      onClose();
                    }}
                    className="p-2.5 rounded-xl bg-slate-950/60 hover:bg-slate-800/60 border border-slate-800 hover:border-blue-500/30 cursor-pointer flex items-center justify-between group transition-all"
                  >
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="text-sm font-semibold text-slate-100 group-hover:text-blue-300">{item.title}</span>
                        <span className="text-xs text-blue-400 font-tamil">({item.title_tamil})</span>
                      </div>
                      <p className="text-xs text-slate-400 line-clamp-1 mt-0.5">{item.desc}</p>
                    </div>
                    <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-blue-400 transition-transform group-hover:translate-x-1 shrink-0 ml-2" />
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Problem Guides Matches */}
          {results.actions && results.actions.length > 0 && (
            <div className="space-y-2">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-purple-400 uppercase tracking-wider">
                <ShieldAlert className="w-3.5 h-3.5" />
                <span>Action Guides ({results.actions.length})</span>
              </div>
              <div className="space-y-1.5">
                {results.actions.map((item) => (
                  <div
                    key={item.id}
                    onClick={() => {
                      onSelectResult('action', item.id);
                      onClose();
                    }}
                    className="p-2.5 rounded-xl bg-slate-950/60 hover:bg-slate-800/60 border border-slate-800 hover:border-purple-500/30 cursor-pointer flex items-center justify-between group transition-all"
                  >
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="text-sm font-semibold text-slate-100 group-hover:text-purple-300">{item.title}</span>
                        <span className="text-xs text-purple-400 font-tamil">({item.title_tamil})</span>
                      </div>
                      <p className="text-xs text-slate-400 line-clamp-1 mt-0.5">{item.desc}</p>
                    </div>
                    <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-purple-400 transition-transform group-hover:translate-x-1 shrink-0 ml-2" />
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
