import React, { useState } from 'react';
import { ShieldCheck, ExternalLink, Calendar, Info, X } from 'lucide-react';

export default function SourceCard({ sources = [] }) {
  const [selectedSource, setSelectedSource] = useState(null);

  if (!sources || sources.length === 0) return null;

  return (
    <div className="mt-4 pt-3 border-t border-slate-800/80">
      <div className="flex items-center gap-2 mb-2 text-xs font-semibold text-slate-400 uppercase tracking-wider">
        <ShieldCheck className="w-3.5 h-3.5 text-brand-cyan" />
        <span>Sources & Verification / சட்ட ஆதாரங்கள்</span>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
        {sources.map((src, idx) => (
          <div
            key={idx}
            className="p-2.5 rounded-lg bg-slate-900/70 border border-slate-800 hover:border-cyan-500/30 transition-all flex items-start justify-between gap-2"
          >
            <div className="space-y-1 text-left">
              <div className="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-cyan-950/60 border border-cyan-500/20 text-cyan-300 inline-block">
                {src.source_type}
              </div>
              <p className="text-xs font-medium text-slate-200 line-clamp-1">{src.source_name}</p>
              {src.legal_section && (
                <p className="text-[11px] text-slate-400 font-mono">{src.legal_section}</p>
              )}
              <div className="flex items-center gap-1 text-[10px] text-slate-500">
                <Calendar className="w-2.5 h-2.5" />
                <span>Verified: {src.last_verified}</span>
              </div>
            </div>

            <button
              onClick={() => setSelectedSource(src)}
              className="shrink-0 mt-1 px-2 py-1 rounded text-[11px] bg-slate-800 hover:bg-cyan-500/20 hover:text-cyan-300 text-slate-300 border border-slate-700/60 transition-colors flex items-center gap-1"
            >
              <span>Verify</span>
              <ExternalLink className="w-2.5 h-2.5" />
            </button>
          </div>
        ))}
      </div>

      {/* Verification Modal */}
      {selectedSource && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm animate-fadeIn">
          <div className="relative w-full max-w-md p-6 rounded-2xl bg-navy-900 border border-cyan-500/30 shadow-2xl text-left space-y-4">
            <button
              onClick={() => setSelectedSource(null)}
              className="absolute top-4 right-4 p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white"
            >
              <X className="w-4 h-4" />
            </button>

            <div className="flex items-center gap-2">
              <div className="p-2 rounded-xl bg-cyan-500/10 text-brand-cyan border border-cyan-500/20">
                <ShieldCheck className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-base font-bold text-white">Source Verification</h3>
                <p className="text-xs text-slate-400 font-mono">{selectedSource.source_type}</p>
              </div>
            </div>

            <div className="p-3.5 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2 text-xs">
              <div>
                <span className="text-slate-400">Statutory Source: </span>
                <span className="font-semibold text-slate-100">{selectedSource.source_name}</span>
              </div>
              {selectedSource.legal_section && (
                <div>
                  <span className="text-slate-400">Section / Provision: </span>
                  <span className="font-mono text-cyan-300">{selectedSource.legal_section}</span>
                </div>
              )}
              <div>
                <span className="text-slate-400">Status: </span>
                <span className="text-amber-400 font-medium">Demo Verified Data</span>
              </div>
              <div className="text-slate-300 text-[11px] leading-relaxed pt-1 border-t border-slate-800">
                {selectedSource.verification_note ||
                  'Demo Source – Replace with verified official source before production.'}
              </div>
            </div>

            <div className="p-3 rounded-xl bg-cyan-950/40 border border-cyan-800/30 flex items-start gap-2.5 text-xs text-cyan-200/90 leading-relaxed">
              <Info className="w-4 h-4 shrink-0 text-brand-cyan mt-0.5" />
              <p>
                <strong>Educational Notice:</strong> Information provided for educational purposes. Laws and procedures may change. Verify important matters with official government/legal gazettes.
              </p>
            </div>

            <div className="flex justify-end pt-1">
              <button
                onClick={() => setSelectedSource(null)}
                className="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-medium text-xs hover:opacity-90 transition-opacity"
              >
                Close Verification
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
