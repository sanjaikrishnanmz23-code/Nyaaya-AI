import React from 'react';
import { Scale, Heart, ShieldCheck, PhoneCall, ExternalLink } from 'lucide-react';

export default function Footer({ onNavigate }) {
  return (
    <footer className="w-full mt-20 border-t border-slate-800/80 bg-navy-950/90 backdrop-blur-md relative z-10 text-slate-400 text-xs">
      {/* Emergency Strip */}
      <div className="border-b border-slate-800/60 bg-gradient-to-r from-red-950/30 via-slate-900/40 to-blue-950/30 py-3 px-4">
        <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3 text-xs">
          <div className="flex items-center gap-2 text-slate-300">
            <PhoneCall className="w-3.5 h-3.5 text-red-400 animate-pulse" />
            <span className="font-semibold text-white">Emergency Helplines:</span>
            <span>Emergency (112)</span>
            <span className="text-slate-600">•</span>
            <span>Cybercrime (1930)</span>
            <span className="text-slate-600">•</span>
            <span>Women (181 / 1091)</span>
            <span className="text-slate-600">•</span>
            <span>Consumer (1915)</span>
          </div>
          <button
            onClick={() => onNavigate('emergency')}
            className="text-cyan-400 hover:text-cyan-300 underline font-medium flex items-center gap-1"
          >
            <span>View All National Helplines</span>
            <ExternalLink className="w-3 h-3" />
          </button>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8 text-left">
          {/* Brand Col */}
          <div className="space-y-3 md:col-span-2">
            <div className="flex items-center gap-2">
              <div className="p-1.5 rounded-lg bg-cyan-500/20 text-brand-cyan border border-cyan-500/30">
                <Scale className="w-4 h-4" />
              </div>
              <span className="text-base font-bold text-white tracking-tight">
                Nyaaya<span className="text-brand-cyan">AI</span>
              </span>
            </div>
            <p className="text-slate-300 text-sm max-w-md font-medium">
              “Technology that helps citizens understand their rights.”
            </p>
            <p className="text-slate-500 text-xs font-tamil">
              “இந்திய குடிமக்களுக்கான இலவச சட்ட மற்றும் உரிமைகள் தகவல் வழிகாட்டி.”
            </p>
            <div className="flex items-center gap-2 pt-2">
              <span className="px-2 py-0.5 rounded-md bg-slate-900 border border-slate-800 text-[10px] text-cyan-300 font-mono">
                Bilingual AI: English ↔ தமிழ்
              </span>
              <span className="px-2 py-0.5 rounded-md bg-slate-900 border border-slate-800 text-[10px] text-purple-300 font-mono">
                Gov-Tech × Open Civic
              </span>
            </div>
          </div>

          {/* Quick Navigation */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold text-white uppercase tracking-wider">Quick Navigation</h4>
            <ul className="space-y-1.5 text-xs">
              <li>
                <button onClick={() => onNavigate('home')} className="hover:text-cyan-300 transition-colors">
                  Home (முகப்பு)
                </button>
              </li>
              <li>
                <button onClick={() => onNavigate('chat')} className="hover:text-cyan-300 transition-colors">
                  Ask NyaayaAI Chat
                </button>
              </li>
              <li>
                <button onClick={() => onNavigate('rights')} className="hover:text-cyan-300 transition-colors">
                  Citizen Rights Explorer (10 Categories)
                </button>
              </li>
              <li>
                <button onClick={() => onNavigate('services')} className="hover:text-cyan-300 transition-colors">
                  Government Services Directory
                </button>
              </li>
              <li>
                <button onClick={() => onNavigate('actions')} className="hover:text-cyan-300 transition-colors">
                  “I Have a Problem. What Can I Do?”
                </button>
              </li>
            </ul>
          </div>

          {/* Trust & Legal */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold text-white uppercase tracking-wider">Statutory Trust</h4>
            <ul className="space-y-1.5 text-xs text-slate-400">
              <li className="flex items-center gap-1.5">
                <ShieldCheck className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
                <span>Verified Statutory References</span>
              </li>
              <li>Supreme Court Directives (D.K. Basu)</li>
              <li>Payment of Wages Act 1936</li>
              <li>Consumer Protection Act 2019</li>
              <li>Right to Information Act 2005</li>
            </ul>
          </div>
        </div>

        {/* Legal Disclaimer Box */}
        <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80 text-left space-y-1.5 mb-6">
          <div className="flex items-center gap-1.5 text-slate-300 font-semibold text-xs">
            <ShieldCheck className="w-3.5 h-3.5 text-amber-400" />
            <span>Important Public Educational Notice:</span>
          </div>
          <p className="text-[11px] text-slate-400 leading-relaxed">
            “NyaayaAI provides general informational content and is not a substitute for professional legal advice or official government guidance. Laws, jurisdictional procedures, and fees may change over time. Always verify important matters with official government portals, official Gazettes, or certified advocates.”
          </p>
          <p className="text-[10px] text-slate-500 font-tamil leading-relaxed">
            “இங்கு வழங்கப்படும் தகவல்கள் விழிப்புணர்வு நோக்கத்திற்காக மட்டுமே. இது சட்ட அல்லது நீதிமன்ற அதிகாரப்பூர்வ ஆலோசனைக்கு மாற்றாகாது.”
          </p>
        </div>

        {/* Bottom Credits */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4 border-t border-slate-800/60 text-slate-500 text-[11px]">
          <div>
            © {new Date().getFullYear()} NyaayaAI. Built with civic purpose for the citizens of India.
          </div>
          <div className="flex items-center gap-1 text-slate-400">
            <span>Made with</span>
            <Heart className="w-3 h-3 text-red-500 fill-red-500" />
            <span>for citizen empowerment</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
