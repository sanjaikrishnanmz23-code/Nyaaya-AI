import React, { useState, useEffect } from 'react';
import { 
  AlertCircle, 
  HelpCircle, 
  Clock, 
  PhoneCall, 
  CheckSquare, 
  ShieldAlert, 
  ArrowRight, 
  CheckCircle2,
  FileCheck,
  ChevronRight,
  Sparkles
} from 'lucide-react';
import { fetchProblems } from '../services/api';

export default function ActionGuidePage({ selectedProblemId }) {
  const [problems, setProblems] = useState([]);
  const [activeProblem, setActiveProblem] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchProblems();
        setProblems(data);
        if (selectedProblemId) {
          const matched = data.find((p) => p.id === selectedProblemId);
          if (matched) setActiveProblem(matched);
          else if (data.length > 0) setActiveProblem(data[0]);
        } else if (data.length > 0) {
          setActiveProblem(data[0]);
        }
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, [selectedProblemId]);

  if (loading) {
    return (
      <div className="py-20 text-center text-slate-400">
        Loading problem resolution roadmaps...
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 text-left">
      {/* Page Header */}
      <div className="space-y-2 pb-6 border-b border-slate-800">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs font-semibold">
          <AlertCircle className="w-3.5 h-3.5 text-amber-400" />
          <span>Interactive Crisis Navigation</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white">
          “I Have a Problem. What Can I Do?”
        </h1>
        <p className="text-sm sm:text-base text-slate-400">
          Select an urgent situation to receive an immediate 4-stage action timeline: <strong className="text-cyan-300">Do this first → Next → Then → Follow up</strong>.
        </p>
        <p className="text-xs sm:text-sm text-cyan-400 font-tamil">
          நெருக்கடியான சூழ்நிலைகளில் நீங்கள் எடுக்க வேண்டிய அவசர மற்றும் சட்டப்பூர்வ நடவடிக்கைகள்
        </p>
      </div>

      {/* Two Column Layout: Problem Selector & Interactive Roadmap */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Left Column: Problem Chooser */}
        <div className="lg:col-span-4 space-y-2.5">
          <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">
            Select Your Situation:
          </h3>
          {problems.map((p) => {
            const isSelected = activeProblem?.id === p.id;
            return (
              <button
                key={p.id}
                onClick={() => setActiveProblem(p)}
                className={`w-full p-4 rounded-2xl text-left border transition-all flex items-center justify-between group ${
                  isSelected
                    ? 'bg-gradient-to-r from-cyan-950/80 via-blue-950/60 to-navy-900 border-cyan-500/50 shadow-glow-cyan'
                    : 'bg-slate-900/60 hover:bg-slate-800/80 border-slate-800 text-slate-300'
                }`}
              >
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <span className={`text-xs font-bold ${isSelected ? 'text-cyan-300' : 'text-slate-100 group-hover:text-cyan-300'}`}>
                      {p.title}
                    </span>
                  </div>
                  <p className="text-[11px] text-slate-400 font-tamil">
                    {p.title_tamil}
                  </p>
                </div>
                <ChevronRight className={`w-4 h-4 shrink-0 transition-transform ${isSelected ? 'text-brand-cyan translate-x-1' : 'text-slate-600'}`} />
              </button>
            );
          })}
        </div>

        {/* Right Column: Progressive Action Roadmap */}
        {activeProblem && (
          <div className="lg:col-span-8 glass-card p-6 sm:p-8 rounded-3xl border border-cyan-500/20 space-y-8">
            {/* Header of Active Problem */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800">
              <div className="space-y-1">
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-red-950/60 border border-red-500/20 text-red-400 uppercase font-semibold">
                  Urgency: {activeProblem.urgency_level}
                </span>
                <h2 className="text-2xl font-bold text-white">
                  {activeProblem.title}
                </h2>
                <p className="text-xs sm:text-sm text-cyan-400 font-tamil">
                  {activeProblem.title_tamil}
                </p>
                <p className="text-xs text-slate-300 pt-1 leading-relaxed">
                  {activeProblem.summary}
                </p>
              </div>

              {activeProblem.helpline && (
                <div className="shrink-0 p-3 rounded-2xl bg-red-950/40 border border-red-500/30 text-center space-y-1">
                  <span className="text-[10px] uppercase font-mono text-red-300 block font-semibold">
                    {activeProblem.helpline_name || "Emergency Line"}
                  </span>
                  <div className="flex items-center justify-center gap-1.5 text-lg font-black text-red-400 font-mono">
                    <PhoneCall className="w-4 h-4" />
                    <span>{activeProblem.helpline}</span>
                  </div>
                </div>
              )}
            </div>

            {/* Visual Action Timeline: Do this first → Next → Then → Follow up */}
            <div className="space-y-4">
              <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
                <Sparkles className="w-3.5 h-3.5 text-brand-cyan" />
                <span>Structured Action Roadmap (செயல் திட்டம்)</span>
              </h3>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {/* 1. Do This First */}
                <div className="p-4 rounded-2xl bg-red-950/20 border border-red-500/20 space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-red-500 text-white font-mono">
                      STAGE 1
                    </span>
                    <h4 className="text-xs font-bold text-red-300 uppercase tracking-wide">
                      Do This First (உடனடி முதல் நடவடிக்கை)
                    </h4>
                  </div>
                  <ul className="space-y-1.5 text-xs text-slate-200">
                    {activeProblem.do_this_first.map((step, idx) => (
                      <li key={idx} className="flex items-start gap-2 leading-relaxed">
                        <span className="text-red-400 font-bold shrink-0">•</span>
                        <span>{step}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* 2. Do Next */}
                <div className="p-4 rounded-2xl bg-amber-950/20 border border-amber-500/20 space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-500 text-slate-950 font-mono">
                      STAGE 2
                    </span>
                    <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wide">
                      Next Step (அடுத்த கட்ட நடவடிக்கை)
                    </h4>
                  </div>
                  <ul className="space-y-1.5 text-xs text-slate-200">
                    {activeProblem.do_next.map((step, idx) => (
                      <li key={idx} className="flex items-start gap-2 leading-relaxed">
                        <span className="text-amber-400 font-bold shrink-0">•</span>
                        <span>{step}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* 3. Then */}
                <div className="p-4 rounded-2xl bg-blue-950/20 border border-blue-500/20 space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-500 text-white font-mono">
                      STAGE 3
                    </span>
                    <h4 className="text-xs font-bold text-blue-300 uppercase tracking-wide">
                      Then (அதிகாரப்பூர்வ புகார் முறை)
                    </h4>
                  </div>
                  <ul className="space-y-1.5 text-xs text-slate-200">
                    {activeProblem.then_step.map((step, idx) => (
                      <li key={idx} className="flex items-start gap-2 leading-relaxed">
                        <span className="text-blue-400 font-bold shrink-0">•</span>
                        <span>{step}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* 4. Follow Up */}
                <div className="p-4 rounded-2xl bg-emerald-950/20 border border-emerald-500/20 space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500 text-slate-950 font-mono">
                      STAGE 4
                    </span>
                    <h4 className="text-xs font-bold text-emerald-300 uppercase tracking-wide">
                      Follow Up (தொடர் சட்ட கண்காணிப்பு)
                    </h4>
                  </div>
                  <ul className="space-y-1.5 text-xs text-slate-200">
                    {activeProblem.follow_up.map((step, idx) => (
                      <li key={idx} className="flex items-start gap-2 leading-relaxed">
                        <span className="text-emerald-400 font-bold shrink-0">•</span>
                        <span>{step}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>

            {/* Documents & Evidence Checklist */}
            <div className="p-5 rounded-2xl bg-slate-950/80 border border-slate-800 space-y-3">
              <div className="flex items-center gap-2 font-bold text-xs text-cyan-300 uppercase tracking-wider">
                <FileCheck className="w-4 h-4 text-brand-cyan" />
                <span>Essential Evidence Checklist (பாதுகாக்க வேண்டிய ஆதாரங்கள்)</span>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-300">
                {activeProblem.documents_checklist.map((doc, idx) => (
                  <div key={idx} className="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center gap-2">
                    <CheckCircle2 className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
                    <span>{doc}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
