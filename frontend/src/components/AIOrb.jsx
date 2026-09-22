import React from 'react';
import { Scale, ShieldCheck, Landmark, Globe, Sparkles } from 'lucide-react';

export default function AIOrb({ size = 'large' }) {
  const isLarge = size === 'large';
  const diameter = isLarge ? 'w-56 h-56 sm:w-72 sm:h-72' : 'w-16 h-16';

  const floatingBadges = [
    { label: 'Citizen Rights', labelTa: 'குடிமக்கள் உரிமை', icon: Scale, position: 'top-2 -left-6 sm:-left-12' },
    { label: 'Legal Information', labelTa: 'சட்ட விழிப்புணர்வு', icon: ShieldCheck, position: 'top-10 -right-6 sm:-right-12' },
    { label: 'Government Services', labelTa: 'அரசு சேவைகள்', icon: Landmark, position: 'bottom-8 -left-8 sm:-left-14' },
    { label: 'Bilingual AI', labelTa: 'இருமொழி AI', icon: Globe, position: 'bottom-2 -right-4 sm:-right-10' },
    { label: 'Trusted Sources', labelTa: 'சரிபார்க்கப்பட்டவை', icon: Sparkles, position: '-top-6 left-1/2 -translate-x-1/2' },
  ];

  return (
    <div className="relative flex items-center justify-center select-none py-6">
      {/* Outer ambient glow */}
      <div className={`absolute ${diameter} rounded-full bg-gradient-to-tr from-brand-cyan/25 via-blue-600/20 to-purple-600/25 blur-3xl animate-pulse-glow pointer-events-none`} />

      {/* Orbit ring 1 */}
      {isLarge && (
        <div className="absolute w-80 h-80 sm:w-96 sm:h-96 rounded-full border border-cyan-400/15 border-dashed animate-orb-rotate pointer-events-none" />
      )}

      {/* Orbit ring 2 */}
      {isLarge && (
        <div className="absolute w-64 h-64 sm:w-80 sm:h-80 rounded-full border border-purple-500/15 animate-orb-rotate pointer-events-none" style={{ animationDirection: 'reverse', animationDuration: '28s' }} />
      )}

      {/* Central Glowing Orb Body */}
      <div className={`relative ${diameter} rounded-full p-[2px] bg-gradient-to-b from-brand-cyan via-blue-500 to-purple-600 shadow-glow-cyan shadow-glow-blue transition-transform duration-500 hover:scale-105`}>
        {/* Inner sphere gradient */}
        <div className="w-full h-full rounded-full bg-gradient-to-tr from-navy-950 via-slate-900 to-navy-850 flex items-center justify-center overflow-hidden border border-white/10">
          {/* Internal energetic swirl */}
          <div className="absolute inset-0 bg-radial-at-c from-brand-cyan/20 via-transparent to-transparent animate-pulse" />
          
          {/* Logo / Core symbol */}
          <div className="relative flex flex-col items-center justify-center z-10 text-center">
            <div className="p-3 sm:p-4 rounded-2xl bg-cyan-500/10 border border-cyan-400/30 backdrop-blur-md shadow-inner shadow-cyan-500/20">
              <Scale className={`${isLarge ? 'w-10 h-10 sm:w-14 sm:h-14' : 'w-6 h-6'} text-brand-cyan animate-pulse`} />
            </div>
            {isLarge && (
              <span className="mt-2 text-xs sm:text-sm font-semibold tracking-widest uppercase text-cyan-200/90 font-mono">
                NyaayaAI
              </span>
            )}
          </div>
        </div>
      </div>

      {/* Floating Civic Badges (only on large hero display) */}
      {isLarge && floatingBadges.map((badge, idx) => {
        const Icon = badge.icon;
        return (
          <div
            key={idx}
            className={`absolute ${badge.position} hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-full bg-navy-900/80 border border-cyan-500/20 backdrop-blur-md shadow-glass shadow-cyan-900/30 text-xs text-slate-200 transition-all duration-300 hover:border-cyan-400 hover:scale-105 z-20 animate-float`}
            style={{ animationDelay: `${idx * 1.2}s` }}
          >
            <Icon className="w-3.5 h-3.5 text-brand-cyan" />
            <div className="flex flex-col text-left">
              <span className="font-medium text-slate-100">{badge.label}</span>
              <span className="text-[10px] text-cyan-300/80 font-tamil leading-tight">{badge.labelTa}</span>
            </div>
          </div>
        );
      })}
    </div>
  );
}
