import React from 'react';
import { 
  Scale, 
  MessageSquare, 
  Compass, 
  ArrowRight, 
  ShieldCheck, 
  Sparkles, 
  AlertCircle, 
  CheckCircle2, 
  FileText, 
  Briefcase, 
  Lock, 
  HeartHandshake, 
  Building2, 
  ChevronRight,
  PhoneCall
} from 'lucide-react';
import AIOrb from '../components/AIOrb';

export default function LandingPage({ onNavigate, onAskPrompt, currentLang }) {
  const samplePrompts = [
    { textEn: "Can my employer withhold my salary?", textTa: "எனக்கு சம்பளம் கொடுக்கவில்லை என்றால் என்ன செய்ய வேண்டும்?", icon: Briefcase },
    { textEn: "What are my rights if I am stopped by police?", textTa: "போலீஸ் என்னை தடுத்தால் எனக்கு என்ன உரிமைகள் உள்ளன?", icon: ShieldCheck },
    { textEn: "How do I report online UPI banking fraud?", textTa: "ஆன்லைன் வங்கி மோசடியில் பணம் போனால் என்ன செய்ய வேண்டும்?", icon: Lock },
    { textEn: "How do I file an RTI application in 30 days?", textTa: "RTI மூலம் அரசு அலுவலகத்தில் தகவல் கேட்பது எப்படி?", icon: FileText },
  ];

  const categoryHighlights = [
    { title: "Labour & Worker Rights", titleTa: "தொழிலாளர் உரிமைகள்", icon: Briefcase, desc: "Timely salary, overtime rules, gratuity, and Samadhan portal grievances." },
    { title: "Police & Legal Protections", titleTa: "காவல்துறை சட்ட உரிமைகள்", icon: ShieldCheck, desc: "D.K. Basu arrest protocols, FIR registration rights, and bail assistance." },
    { title: "Digital & Cyber Rights", titleTa: "சைபர் மற்றும் தனியுரிமை", icon: Lock, desc: "Immediate 1930 fraud freeze, DPDP privacy, and online scam remedies." },
    { title: "Consumer Redressal", titleTa: "நுகர்வோர் பாதுகாப்பு", icon: Scale, desc: "Defective goods, e-Daakhil court filing, and warranty protection." },
    { title: "Women & Child Rights", titleTa: "பெண்கள் மற்றும் குழந்தைகள்", icon: HeartHandshake, desc: "Domestic Violence Act, POSH workplace committees, and 181 shelter help." },
    { title: "Government Transparency", titleTa: "தகவல் அறியும் உரிமை (RTI)", icon: Building2, desc: "Demand certified copies, inspect works, and file appeals under RTI 2005." },
  ];

  return (
    <div className="space-y-24 py-6 sm:py-12">
      {/* 1. Hero Section */}
      <section className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
        {/* Bilingual badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-cyan-950/70 border border-cyan-500/30 text-cyan-300 text-xs font-mono shadow-sm animate-pulse">
          <Sparkles className="w-3.5 h-3.5 text-brand-cyan" />
          <span>Generative AI Civic Assistant • English ↔ தமிழ்</span>
        </div>

        {/* Main Headline */}
        <div className="max-w-4xl mx-auto space-y-4">
          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-black tracking-tight leading-[1.1]">
            Know Your Rights.{' '}
            <span className="text-gradient-cyan block sm:inline">Know Your Voice.</span>
          </h1>
          <p className="text-lg sm:text-2xl text-cyan-200/90 font-tamil font-medium">
            “உங்கள் உரிமைகளை அறிந்திடுங்கள். உங்கள் குரலை ஓங்கிடுங்கள்.”
          </p>
          <p className="max-w-2xl mx-auto text-sm sm:text-base text-slate-300 leading-relaxed pt-2">
            An AI-powered citizen rights information assistant that explains constitutional rights, statutory procedures, and public services in simple bilingual language.
          </p>
        </div>

        {/* CTAs */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-2">
          <button
            onClick={() => onNavigate('chat')}
            className="w-full sm:w-auto px-8 py-3.5 rounded-2xl bg-gradient-to-r from-cyan-500 via-blue-600 to-purple-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold text-sm sm:text-base flex items-center justify-center gap-2.5 shadow-glow-cyan hover:scale-[1.02] transition-all"
          >
            <MessageSquare className="w-5 h-5" />
            <span>Ask NyaayaAI</span>
            <ArrowRight className="w-4 h-4 ml-1" />
          </button>

          <button
            onClick={() => onNavigate('rights')}
            className="w-full sm:w-auto px-7 py-3.5 rounded-2xl bg-slate-900/90 hover:bg-slate-800 border border-slate-700/80 hover:border-cyan-500/40 text-slate-200 font-semibold text-sm sm:text-base flex items-center justify-center gap-2 transition-all"
          >
            <Compass className="w-5 h-5 text-brand-cyan" />
            <span>Explore Citizen Rights</span>
          </button>
        </div>

        {/* Glowing AI Orb Visual Centerpiece */}
        <div className="pt-6 sm:pt-10">
          <AIOrb size="large" />
        </div>

        {/* Interactive Quick Question Prompts */}
        <div className="max-w-4xl mx-auto pt-6 text-left">
          <p className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3 flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-brand-cyan" />
            <span>Try Asking NyaayaAI (Click to test):</span>
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {samplePrompts.map((item, idx) => {
              const Icon = item.icon;
              return (
                <button
                  key={idx}
                  onClick={() => onAskPrompt(item.textEn)}
                  className="p-3.5 rounded-xl bg-slate-900/60 hover:bg-slate-800/80 border border-slate-800 hover:border-cyan-500/40 text-left group transition-all flex items-start gap-3 shadow-sm hover:-translate-y-0.5"
                >
                  <div className="p-2 rounded-lg bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 group-hover:scale-110 transition-transform shrink-0">
                    <Icon className="w-4 h-4" />
                  </div>
                  <div className="space-y-1">
                    <p className="text-xs sm:text-sm font-semibold text-slate-100 group-hover:text-cyan-300">
                      "{item.textEn}"
                    </p>
                    <p className="text-[11px] text-cyan-300/80 font-tamil">
                      "{item.textTa}"
                    </p>
                  </div>
                </button>
              );
            })}
          </div>
        </div>
      </section>

      {/* 2. Educational Trust & Statutory Integrity Strip */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-cyan-500/20 relative overflow-hidden">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6 text-left">
            <div className="space-y-2 max-w-2xl">
              <div className="flex items-center gap-2 text-cyan-400 font-semibold text-xs uppercase tracking-wider">
                <ShieldCheck className="w-4 h-4 text-brand-cyan" />
                <span>Statutory Trust & Educational Purpose</span>
              </div>
              <h2 className="text-xl sm:text-2xl font-bold text-white">
                Legal Clarity Without The Confusing Jargon.
              </h2>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                Every response is structured with step-by-step actions, relevant statutory citations, designated public authorities, and an authentic Tamil translation.
              </p>
            </div>

            <div className="grid grid-cols-2 gap-3 w-full md:w-auto shrink-0">
              <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-center">
                <span className="text-2xl font-black text-brand-cyan">10+</span>
                <p className="text-[11px] text-slate-400">Statutory Categories</p>
              </div>
              <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-center">
                <span className="text-2xl font-black text-purple-400">100%</span>
                <p className="text-[11px] text-slate-400">Bilingual English + தமிழ்</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 3. Rights Explorer Preview Grid */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-left space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
          <div>
            <div className="text-xs font-semibold text-brand-cyan uppercase tracking-wider mb-1">
              Explore Your Protections
            </div>
            <h2 className="text-2xl sm:text-3xl font-bold text-white">
              10 Fundamental & Civic Rights Categories
            </h2>
            <p className="text-xs sm:text-sm text-slate-400 font-tamil">
              அரசியலமைப்பு மற்றும் இந்திய சட்டங்களின் கீழ் குடிமக்களுக்கு உள்ள உரிமைகள்
            </p>
          </div>

          <button
            onClick={() => onNavigate('rights')}
            className="text-xs font-semibold text-cyan-400 hover:text-cyan-300 flex items-center gap-1.5 self-start sm:self-auto"
          >
            <span>View All 10 Categories</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {categoryHighlights.map((cat, idx) => {
            const Icon = cat.icon;
            return (
              <div
                key={idx}
                onClick={() => onNavigate('rights')}
                className="glass-card p-5 rounded-2xl cursor-pointer group flex flex-col justify-between space-y-4"
              >
                <div className="space-y-3">
                  <div className="p-2.5 rounded-xl bg-cyan-500/10 border border-cyan-500/20 text-brand-cyan w-fit group-hover:scale-110 transition-transform">
                    <Icon className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="text-base font-bold text-slate-100 group-hover:text-cyan-300 transition-colors">
                      {cat.title}
                    </h3>
                    <p className="text-xs text-cyan-400/90 font-tamil mt-0.5">
                      {cat.titleTa}
                    </p>
                  </div>
                  <p className="text-xs text-slate-400 leading-relaxed">
                    {cat.desc}
                  </p>
                </div>

                <div className="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400 group-hover:text-cyan-300">
                  <span>Explore Statutory Remedies</span>
                  <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 4. Guided Problem Solver Callout */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-left">
        <div className="p-8 sm:p-10 rounded-3xl bg-gradient-to-r from-navy-900 via-blue-950/70 to-navy-900 border border-cyan-500/30 shadow-2xl relative overflow-hidden">
          <div className="max-w-2xl space-y-4 relative z-10">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 text-xs font-semibold">
              <AlertCircle className="w-3.5 h-3.5 text-brand-cyan" />
              <span>Interactive Citizen Roadmap</span>
            </div>
            <h2 className="text-2xl sm:text-4xl font-extrabold text-white">
              “I Have a Problem. What Can I Do?”
            </h2>
            <p className="text-xs sm:text-base text-slate-300 leading-relaxed">
              Facing an acute issue right now? Get an exact 4-step progressive action timeline:
              <br />
              <strong className="text-cyan-300">Do this first → Next → Then → Follow up</strong>
            </p>
            <div className="flex flex-wrap gap-2 pt-2">
              {['Salary Withheld', 'UPI Fraud', 'Police Questioning', 'Consumer Issue', 'RTI Appeal'].map((item) => (
                <span key={item} className="px-2.5 py-1 rounded-lg bg-slate-900/80 border border-slate-700 text-xs text-slate-300">
                  {item}
                </span>
              ))}
            </div>
            <div className="pt-4">
              <button
                onClick={() => onNavigate('actions')}
                className="px-6 py-3 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-navy-950 font-bold text-sm flex items-center gap-2 transition-all shadow-glow-cyan"
              >
                <span>Launch Guided Problem Solver</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* 5. Emergency Helpline Strip */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-left space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <PhoneCall className="w-4 h-4 text-red-400" />
            <h3 className="text-base font-bold text-white">Emergency National Helplines (அவசர உதவி எண்கள்)</h3>
          </div>
          <button
            onClick={() => onNavigate('emergency')}
            className="text-xs text-cyan-400 hover:underline"
          >
            View Directory
          </button>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {[
            { name: "All Emergencies", number: "112", sub: "Police, Fire, Medical", color: "text-red-400" },
            { name: "Cyber Crime", number: "1930", sub: "Financial Fraud", color: "text-amber-400" },
            { name: "Women Helpline", number: "181 / 1091", sub: "Safety & Abuse", color: "text-pink-400" },
            { name: "Free Legal Aid", number: "15100", sub: "NALSA Counsel", color: "text-cyan-400" },
          ].map((item, idx) => (
            <div key={idx} className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-left space-y-1">
              <span className="text-xs text-slate-400">{item.name}</span>
              <p className={`text-xl sm:text-2xl font-black ${item.color} font-mono tracking-tight`}>{item.number}</p>
              <p className="text-[10px] text-slate-500">{item.sub}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
