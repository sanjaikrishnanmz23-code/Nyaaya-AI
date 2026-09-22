import React, { useState, useEffect } from 'react';
import { 
  Scale, 
  Briefcase, 
  ShoppingCart, 
  ShieldAlert, 
  Lock, 
  HeartHandshake, 
  FileText, 
  GraduationCap, 
  Activity, 
  Trees, 
  Search, 
  X, 
  ExternalLink, 
  CheckCircle2, 
  ArrowRight,
  ShieldCheck,
  FileCheck2,
  Building2
} from 'lucide-react';
import { fetchCategories } from '../services/api';
import SourceCard from '../components/SourceCard';

// Map icon strings to Lucide components
const iconMap = {
  Scale,
  Briefcase,
  ShoppingCart,
  ShieldAlert,
  Lock,
  HeartHandshake,
  FileText,
  GraduationCap,
  Activity,
  Trees,
};

export default function RightsExplorer({ onAskQuestion, selectedCatId }) {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [activeCategory, setActiveCategory] = useState(null);

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchCategories();
        setCategories(data);
        if (selectedCatId) {
          const matched = data.find((c) => c.id === selectedCatId);
          if (matched) setActiveCategory(matched);
        }
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, [selectedCatId]);

  const filteredCategories = categories.filter((cat) => {
    if (!search.trim()) return true;
    const q = search.toLowerCase();
    return (
      cat.title.toLowerCase().includes(q) ||
      cat.title_tamil.toLowerCase().includes(q) ||
      cat.short_desc.toLowerCase().includes(q)
    );
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 text-left">
      {/* Page Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6 border-b border-slate-800">
        <div className="space-y-2">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 text-xs font-semibold">
            <Scale className="w-3.5 h-3.5 text-brand-cyan" />
            <span>Constitutional & Statutory Code</span>
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold text-white">
            Citizen Rights Explorer
          </h1>
          <p className="text-sm sm:text-base text-slate-400">
            Comprehensive guide to Indian fundamental freedoms, labour protections, consumer rights, and statutory remedies.
          </p>
          <p className="text-xs sm:text-sm text-cyan-400/90 font-tamil">
            இந்திய குடிமக்களுக்கான 10 முதன்மை சட்ட உரிமைகள் மற்றும் பாதுகாப்பு வழிமுறைகள்
          </p>
        </div>

        {/* Search input */}
        <div className="relative w-full md:w-80">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search rights (e.g. wages, bail, rti)..."
            className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900 border border-slate-700/80 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-400"
          />
        </div>
      </div>

      {/* Grid of 10 Category Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredCategories.map((cat) => {
          const Icon = iconMap[cat.icon] || Scale;
          return (
            <div
              key={cat.id}
              className="glass-card p-6 rounded-2xl flex flex-col justify-between space-y-4 hover:border-cyan-500/40 group transition-all"
            >
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <div className="p-3 rounded-xl bg-cyan-500/10 text-brand-cyan border border-cyan-500/20 group-hover:scale-110 transition-transform">
                    <Icon className="w-6 h-6" />
                  </div>
                  <span className="text-[11px] font-mono font-semibold px-2 py-0.5 rounded bg-slate-900 text-slate-300 border border-slate-800">
                    {cat.badge}
                  </span>
                </div>

                <div>
                  <h3 className="text-lg font-bold text-white group-hover:text-cyan-300 transition-colors">
                    {cat.title}
                  </h3>
                  <p className="text-xs text-cyan-400 font-tamil mt-0.5">
                    {cat.title_tamil}
                  </p>
                </div>

                <p className="text-xs text-slate-300 leading-relaxed">
                  {cat.short_desc}
                </p>
                <p className="text-[11px] text-slate-400 font-tamil leading-relaxed">
                  {cat.short_desc_tamil}
                </p>
              </div>

              <div className="pt-3 border-t border-slate-800/80 flex items-center justify-between">
                <button
                  onClick={() => setActiveCategory(cat)}
                  className="w-full py-2.5 rounded-xl bg-slate-900 hover:bg-gradient-to-r hover:from-cyan-500 hover:to-blue-600 text-slate-200 hover:text-white font-semibold text-xs transition-all border border-slate-700/80 flex items-center justify-center gap-2"
                >
                  <span>Explore Remedies & Citations</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          );
        })}
      </div>

      {/* Deep Detail Modal for Selected Category */}
      {activeCategory && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md overflow-y-auto animate-fadeIn">
          <div className="relative w-full max-w-3xl my-8 p-6 sm:p-8 rounded-3xl bg-navy-900 border border-cyan-500/30 shadow-2xl text-left space-y-6 max-h-[90vh] overflow-y-auto">
            {/* Close Button */}
            <button
              onClick={() => setActiveCategory(null)}
              className="absolute top-5 right-5 p-2 rounded-xl bg-slate-800 text-slate-400 hover:text-white transition-colors"
            >
              <X className="w-5 h-5" />
            </button>

            {/* Modal Header */}
            <div className="flex items-start gap-4">
              <div className="p-3.5 rounded-2xl bg-cyan-500/10 text-brand-cyan border border-cyan-500/30 shrink-0">
                <Scale className="w-8 h-8" />
              </div>
              <div className="space-y-1 pr-10">
                <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-950/60 border border-cyan-500/30 text-cyan-300">
                  {activeCategory.badge}
                </span>
                <h2 className="text-xl sm:text-2xl font-black text-white">
                  {activeCategory.title}
                </h2>
                <p className="text-sm text-cyan-400 font-tamil">
                  {activeCategory.title_tamil}
                </p>
              </div>
            </div>

            {/* Overview */}
            <div className="p-4 rounded-2xl bg-slate-950/60 border border-slate-800 space-y-2">
              <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Overview & Constitutional Guarantee
              </h4>
              <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
                {activeCategory.overview}
              </p>
              <p className="text-xs sm:text-sm text-slate-400 font-tamil leading-relaxed pt-1 border-t border-slate-800">
                {activeCategory.overview_tamil}
              </p>
            </div>

            {/* Citizen Action Steps */}
            <div className="space-y-2">
              <h4 className="text-xs font-bold text-cyan-300 uppercase tracking-wider">
                What Citizens Can Do (உடனடி நடவடிக்கைகள்)
              </h4>
              <div className="space-y-2">
                {activeCategory.citizen_actions.map((act, idx) => (
                  <div key={idx} className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 text-xs text-slate-200 flex items-start gap-2.5">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                    <span>{act}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Common Questions Accordion */}
            {activeCategory.common_questions && activeCategory.common_questions.length > 0 && (
              <div className="space-y-3">
                <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                  Frequently Addressed Questions
                </h4>
                <div className="space-y-2.5">
                  {activeCategory.common_questions.map((qItem, idx) => (
                    <div key={idx} className="p-3.5 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs">
                      <div className="font-bold text-slate-100 flex items-center justify-between">
                        <span>{qItem.q}</span>
                        {onAskQuestion && (
                          <button
                            onClick={() => {
                              onAskQuestion(qItem.q);
                              setActiveCategory(null);
                            }}
                            className="text-[11px] text-cyan-400 hover:underline flex items-center gap-1"
                          >
                            <span>Ask AI</span>
                            <ArrowRight className="w-3 h-3" />
                          </button>
                        )}
                      </div>
                      <p className="text-slate-300 leading-relaxed">{qItem.a}</p>
                      <p className="text-slate-400 font-tamil pt-1 border-t border-slate-800 leading-relaxed">
                        {qItem.a_ta}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Relevant Authorities & Required Documents */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="p-3.5 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2 text-xs">
                <div className="flex items-center gap-2 font-bold text-blue-300">
                  <Building2 className="w-4 h-4" />
                  <span>Designated Public Authorities</span>
                </div>
                <ul className="space-y-1 text-slate-300 list-disc list-inside">
                  {activeCategory.relevant_authorities.map((auth, idx) => (
                    <li key={idx}>{auth}</li>
                  ))}
                </ul>
              </div>

              <div className="p-3.5 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2 text-xs">
                <div className="flex items-center gap-2 font-bold text-purple-300">
                  <FileCheck2 className="w-4 h-4" />
                  <span>Important Documents & Evidence</span>
                </div>
                <ul className="space-y-1 text-slate-300 list-disc list-inside">
                  {activeCategory.important_documents.map((doc, idx) => (
                    <li key={idx}>{doc}</li>
                  ))}
                </ul>
              </div>
            </div>

            {/* Statutory Sources & Citations */}
            {activeCategory.official_sources && (
              <SourceCard sources={activeCategory.official_sources} />
            )}

            {/* Modal Actions */}
            <div className="flex flex-col sm:flex-row items-center justify-end gap-3 pt-3 border-t border-slate-800">
              {onAskQuestion && (
                <button
                  onClick={() => {
                    onAskQuestion(`What are my rights regarding ${activeCategory.title}?`);
                    setActiveCategory(null);
                  }}
                  className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-semibold text-xs flex items-center justify-center gap-2 shadow-glow-cyan"
                >
                  <span>Ask NyaayaAI about {activeCategory.title}</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              )}
              <button
                onClick={() => setActiveCategory(null)}
                className="w-full sm:w-auto px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium"
              >
                Close Window
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
