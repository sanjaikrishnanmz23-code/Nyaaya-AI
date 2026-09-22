import React, { useState, useEffect } from 'react';
import { 
  LayoutDashboard, 
  Clock, 
  Bookmark, 
  Trash2, 
  Languages, 
  ArrowRight, 
  MessageSquare,
  Sparkles,
  ShieldCheck
} from 'lucide-react';
import { fetchHistory, clearHistoryApi } from '../services/api';

export default function DashboardPage({ currentLang, setCurrentLang, savedBookmarks = [], onClearBookmarks, onAskQuestion }) {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchHistory();
        setHistory(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  const handleClearHistory = async () => {
    if (confirm('Are you sure you want to clear your local query history?')) {
      try {
        await clearHistoryApi();
        setHistory([]);
      } catch (err) {
        console.error(err);
      }
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 text-left">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 pb-6 border-b border-slate-800">
        <div className="space-y-2">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/10 border border-purple-500/20 text-purple-300 text-xs font-semibold">
            <LayoutDashboard className="w-3.5 h-3.5 text-purple-400" />
            <span>Citizen Privacy & Personal History</span>
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold text-white">
            User Dashboard
          </h1>
          <p className="text-sm sm:text-base text-slate-400">
            View your recent queries, bookmarked legal answers, and language preferences. No personal login or tracking required.
          </p>
        </div>

        <button
          onClick={handleClearHistory}
          className="px-4 py-2 rounded-xl bg-slate-900 hover:bg-red-950/40 text-slate-400 hover:text-red-400 border border-slate-800 text-xs font-semibold transition-colors flex items-center gap-2 self-start sm:self-auto"
        >
          <Trash2 className="w-4 h-4" />
          <span>Clear Query History</span>
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column: Recent Questions */}
        <div className="lg:col-span-2 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <Clock className="w-4 h-4 text-cyan-400" />
              <span>Recent Questions ({history.length})</span>
            </h3>
          </div>

          {history.length === 0 ? (
            <div className="glass-card p-8 rounded-2xl text-center text-slate-400 space-y-2">
              <MessageSquare className="w-8 h-8 mx-auto text-slate-600" />
              <p className="text-sm">No recent queries recorded yet.</p>
              <p className="text-xs text-slate-500">Ask a question to see your history here.</p>
            </div>
          ) : (
            <div className="space-y-3">
              {history.map((item) => (
                <div
                  key={item.id}
                  className="glass-card p-4 rounded-xl border border-slate-800 flex items-start justify-between gap-4"
                >
                  <div className="space-y-1">
                    <p className="text-xs font-bold text-slate-100">{item.question}</p>
                    <p className="text-[11px] text-slate-400 line-clamp-2">
                      {item.response.simple_explanation}
                    </p>
                    <span className="text-[10px] text-slate-500 font-mono">
                      {new Date(item.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} • Lang: {item.language}
                    </span>
                  </div>

                  {onAskQuestion && (
                    <button
                      onClick={() => onAskQuestion(item.question)}
                      className="shrink-0 p-2 rounded-lg bg-slate-900 text-cyan-400 hover:bg-cyan-500/20 border border-slate-800"
                      title="Ask again"
                    >
                      <ArrowRight className="w-4 h-4" />
                    </button>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Right Column: Preferences & Bookmarks */}
        <div className="space-y-6">
          {/* Preferences Card */}
          <div className="glass-card p-5 rounded-2xl border border-slate-800 space-y-3">
            <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
              <Languages className="w-4 h-4 text-brand-cyan" />
              <span>Default Language Preference</span>
            </h3>
            <p className="text-xs text-slate-400">
              Choose your preferred language for AI responses:
            </p>
            <div className="flex gap-2">
              {['en', 'ta', 'both'].map((lang) => (
                <button
                  key={lang}
                  onClick={() => setCurrentLang(lang)}
                  className={`flex-1 py-1.5 rounded-lg text-xs font-semibold capitalize border transition-all ${
                    currentLang === lang
                      ? 'bg-cyan-500/20 text-cyan-300 border-cyan-400 shadow-sm'
                      : 'bg-slate-900 text-slate-400 border-slate-800 hover:text-white'
                  }`}
                >
                  {lang === 'both' ? 'Both (இரண்டும்)' : lang === 'ta' ? 'தமிழ்' : 'English'}
                </button>
              ))}
            </div>
          </div>

          {/* Bookmarks Card */}
          <div className="glass-card p-5 rounded-2xl border border-slate-800 space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
                <Bookmark className="w-4 h-4 text-amber-400" />
                <span>Saved Answers ({savedBookmarks.length})</span>
              </h3>
              {savedBookmarks.length > 0 && onClearBookmarks && (
                <button onClick={onClearBookmarks} className="text-[11px] text-red-400 hover:underline">
                  Clear
                </button>
              )}
            </div>

            {savedBookmarks.length === 0 ? (
              <p className="text-xs text-slate-500 py-4 text-center">
                Click the bookmark icon on any AI answer to save it here for offline reference.
              </p>
            ) : (
              <div className="space-y-2">
                {savedBookmarks.map((b, idx) => (
                  <div key={idx} className="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs">
                    <p className="font-semibold text-slate-200">{b.title}</p>
                    <span className="text-[10px] text-slate-500">{b.item_type}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
