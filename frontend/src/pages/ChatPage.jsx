import React, { useState, useEffect, useRef } from 'react';
import { 
  Send, 
  Mic, 
  MicOff, 
  Trash2, 
  Copy, 
  Volume2, 
  VolumeX, 
  Bookmark, 
  BookmarkCheck, 
  Scale, 
  ShieldCheck, 
  Info, 
  Sparkles, 
  Check, 
  ArrowRight,
  Loader2,
  ExternalLink,
  ChevronDown,
  ChevronUp
} from 'lucide-react';
import { askQuestion } from '../services/api';
import { speakText, stopSpeaking, createSpeechRecognizer } from '../utils/speech';
import LanguageSelector from '../components/LanguageSelector';
import SourceCard from '../components/SourceCard';

export default function ChatPage({ initialPrompt, currentLang, setCurrentLang, onSaveBookmark, savedBookmarks = [] }) {
  const [messages, setMessages] = useState([
    {
      id: 'welcome',
      sender: 'ai',
      text: null,
      data: {
        question: "Welcome to NyaayaAI Citizen Rights Assistant",
        simple_explanation: "Hello! I am your AI Citizen Rights Assistant. Ask me any question regarding your rights under Indian law, employer disputes, police encounters, consumer issues, RTI applications, or government services. I explain everything in simple bilingual language (English and தமிழ்).",
        what_you_can_do: [
            "1. Type your question freely in English, Tamil, or Tanglish.",
            "2. Switch between English, Tamil, or Both at any time using the selector above.",
            "3. Click any suggested question below to see an instant structured legal breakdown.",
            "4. Listen to the answers using the bilingual audio speaker button."
        ],
        your_rights: [
            "Right to Information & Public Service Accountability (RTI Act 2005)",
            "Right to Fair Administrative Treatment & Natural Justice (Article 14, 21)",
            "Right to Free Legal Services under National Legal Services Authorities Act (NALSA)"
        ],
        where_to_get_help: [
            "National Emergency Helpline: 112",
            "National Legal Services Authority (NALSA): 15100",
            "National Consumer Helpline: 1915",
            "Cyber Fraud Reporting: 1930"
        ],
        tamil_explanation: "வணக்கம்! நான் உங்கள் நியாயாAI (NyaayaAI) குடிமக்கள் உரிமைகள் உதவியாளர். உங்கள் அடிப்படை உரிமைகள், சம்பள பாக்கி, காவல்துறை விசாரணை, நுகர்வோர் குறைபாடுகள் அல்லது அரசு சான்றிதழ்கள் குறித்து என்னிடம் தமிழில் அல்லது ஆங்கிலத்தில் கேளுங்கள். தெளிவான சட்ட வழிகாட்டுதலை உடனே பெறலாம்.",
        tamil_steps: [
            "1. உங்கள் கேள்வியை கீழே உள்ள கட்டத்தில் தட்டச்சு செய்யவும்.",
            "2. மேலே உள்ள பொத்தான் மூலம் தமிழ், ஆங்கிலம் அல்லது இரண்டையும் தேர்ந்தெடுக்கலாம்.",
            "3. கீழே உள்ள மாதிரி கேள்விகளை கிளிக் செய்து உடனடியாக விளக்கம் பெறலாம்.",
            "4. 'ஸ்பீக்கர்' பொத்தானை அழுத்தி தமிழ் அல்லது ஆங்கிலத்தில் பதிலை கேட்கலாம்."
        ],
        disclaimer: "Information provided for educational purposes. Laws and procedures may change. Verify important matters with official government/legal sources.",
        sources: [
            {
                source_type: "Statutory Legal Aid Enactment",
                source_name: "Legal Services Authorities Act, 1987",
                legal_section: "Section 12",
                last_verified: "National Legal Services Authority",
                verification_note: "Provides free legal counsel to citizens meeting statutory criteria."
            }
        ]
      }
    }
  ]);

  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [speakingMsgId, setSpeakingMsgId] = useState(null);
  const [copiedId, setCopiedId] = useState(null);
  const [expandedSections, setExpandedSections] = useState({});

  const messagesEndRef = useRef(null);
  const recognitionRef = useRef(null);

  const suggestedQuestions = [
    { text: "Can my employer withhold my salary?", lang: "en" },
    { text: "What are my rights if I am stopped by police?", lang: "en" },
    { text: "How do I report online UPI banking fraud?", lang: "en" },
    { text: "How do I file a consumer complaint for a defective product?", lang: "en" },
    { text: "எனக்கு சம்பளம் கொடுக்கவில்லை என்றால் என்ன செய்ய வேண்டும்?", lang: "ta" },
    { text: "போலீஸ் என்னை தடுத்தால் எனக்கு என்ன உரிமைகள் உள்ளன?", lang: "ta" },
    { text: "எனது அடிப்படை உரிமைகள் என்ன?", lang: "ta" },
    { text: "RTI மூலம் அரசு அலுவலகத்தில் தகவல் கேட்பது எப்படி?", lang: "ta" },
  ];

  // Auto-scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  // Handle incoming initial prompt from Landing Page
  useEffect(() => {
    if (initialPrompt && initialPrompt.trim()) {
      handleSend(initialPrompt);
    }
  }, [initialPrompt]);

  const handleSend = async (questionText = null) => {
    const textToSend = questionText || input;
    if (!textToSend || !textToSend.trim() || loading) return;

    const userMsg = {
      id: Date.now().toString(),
      sender: 'user',
      text: textToSend.trim(),
    };

    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const responseData = await askQuestion(textToSend.trim(), currentLang);
      const aiMsg = {
        id: (Date.now() + 1).toString(),
        sender: 'ai',
        data: responseData,
      };
      setMessages((prev) => [...prev, aiMsg]);
    } catch (err) {
      const errorMsg = {
        id: (Date.now() + 1).toString(),
        sender: 'ai',
        data: {
          question: textToSend,
          simple_explanation: "I encountered a network difficulty connecting to the civic knowledge engine. Please check your connection or retry your question.",
          what_you_can_do: ["1. Refresh the page or test your internet connection.", "2. Re-phrase your question with clear civic terms.", "3. Contact official emergency numbers if immediate help is required."],
          your_rights: ["Right to Information & due process"],
          where_to_get_help: ["National Emergency: 112"],
          tamil_explanation: "மன்னிக்கவும், தகவல்களைப் பெறுவதில் தற்காலிக பிழை ஏற்பட்டுள்ளது. தயவுசெய்து சிறிது நேரம் கழித்து மீண்டும் முயற்சிக்கவும்.",
          tamil_steps: ["1. இணைய இணைப்பை சரிபார்க்கவும்.", "2. உங்கள் கேள்வியை மீண்டும் அனுப்பவும்."],
          disclaimer: "Information provided for educational purposes.",
          sources: []
        }
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setLoading(false);
    }
  };

  // Toggle Voice Input
  const toggleRecording = () => {
    if (isRecording) {
      if (recognitionRef.current) {
        recognitionRef.current.stop();
      }
      setIsRecording(false);
      return;
    }

    const rec = createSpeechRecognizer(
      currentLang === 'ta' ? 'ta' : 'en',
      (transcript) => {
        setInput(transcript);
        setIsRecording(false);
      },
      (err) => {
        console.warn('Speech error:', err);
        setIsRecording(false);
      },
      () => setIsRecording(false)
    );

    if (rec) {
      recognitionRef.current = rec;
      rec.start();
      setIsRecording(true);
    } else {
      alert('Speech Recognition is not supported on this browser. Please use Chrome, Edge, or Safari.');
    }
  };

  // Handle Text-To-Speech
  const handleTTS = (msgId, text, lang) => {
    if (speakingMsgId === msgId) {
      stopSpeaking();
      setSpeakingMsgId(null);
      return;
    }

    setSpeakingMsgId(msgId);
    speakText(text, lang, () => {
      setSpeakingMsgId(null);
    });
  };

  // Copy Answer Text
  const handleCopy = (msgId, data) => {
    const formatted = `NyaayaAI - Citizen Rights Answer
Question: ${data.question}

EXPLANATION:
${data.simple_explanation}

ACTIONS:
${data.what_you_can_do.join('\n')}

YOUR RIGHTS:
${data.your_rights.join('\n')}

TAMIL EXPLANATION:
${data.tamil_explanation}

Important: ${data.disclaimer}`;

    navigator.clipboard.writeText(formatted);
    setCopiedId(msgId);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const clearChat = () => {
    stopSpeaking();
    setSpeakingMsgId(null);
    setMessages([messages[0]]);
  };

  const toggleExpand = (key) => {
    setExpandedSections((prev) => ({ ...prev, [key]: !prev[key] }));
  };

  return (
    <div className="max-w-5xl mx-auto px-3 sm:px-6 py-4 flex flex-col h-[calc(100vh-5rem)]">
      {/* Header bar */}
      <div className="glass-panel px-4 py-3 rounded-2xl mb-3 flex flex-wrap items-center justify-between gap-3 border border-cyan-500/20">
        <div className="flex items-center gap-3 text-left">
          <div className="relative p-2 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-brand-cyan">
            <Scale className="w-5 h-5 animate-pulse" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-sm sm:text-base font-bold text-white">NyaayaAI Assistant</h2>
              <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1 animate-pulse" />
                Live Engine
              </span>
            </div>
            <p className="text-[11px] text-slate-400">
              Indian Citizen Rights & Statutory Remedies • குடிமக்கள் உரிமைகள்
            </p>
          </div>
        </div>

        {/* Language selector & Chat Actions */}
        <div className="flex items-center gap-2">
          <LanguageSelector
            currentLang={currentLang}
            onChange={(lang) => {
              setCurrentLang(lang);
              stopSpeaking();
              setSpeakingMsgId(null);
            }}
            compact={true}
          />

          <button
            onClick={clearChat}
            className="p-1.5 rounded-lg bg-slate-900/80 hover:bg-red-950/40 text-slate-400 hover:text-red-400 border border-slate-800 transition-colors"
            title="Clear Chat History"
          >
            <Trash2 className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Messages Scroll Area */}
      <div className="flex-1 overflow-y-auto px-1 py-2 space-y-4 pr-2">
        {messages.map((msg) => {
          if (msg.sender === 'user') {
            return (
              <div key={msg.id} className="flex justify-end">
                <div className="max-w-[85%] sm:max-w-[70%] p-3.5 rounded-2xl rounded-tr-none bg-gradient-to-r from-cyan-600 to-blue-600 text-white shadow-md text-left text-sm leading-relaxed">
                  <p className="font-medium">{msg.text}</p>
                </div>
              </div>
            );
          }

          // AI Response Bubble
          const data = msg.data;
          const isSpeaking = speakingMsgId === msg.id;
          const isSaved = savedBookmarks.some((b) => b.item_id === msg.id);

          // Decide what sections to display based on currentLang
          const showEn = currentLang === 'en' || currentLang === 'both';
          const showTa = currentLang === 'ta' || currentLang === 'both';

          return (
            <div key={msg.id} className="flex justify-start">
              <div className="max-w-full sm:max-w-[92%] glass-card p-4 sm:p-6 rounded-2xl rounded-tl-none border border-cyan-500/20 text-left space-y-4 shadow-glass">
                {/* Header with question title and action tools */}
                <div className="flex items-start justify-between gap-3 pb-3 border-b border-slate-800">
                  <div className="space-y-0.5">
                    <span className="text-[10px] font-mono uppercase tracking-wider text-cyan-400">
                      Citizen Rights Information / கல்வி வழிகாட்டல்
                    </span>
                    <h3 className="text-sm sm:text-base font-bold text-white">
                      {data.question}
                    </h3>
                  </div>

                  {/* Actions: TTS, Copy, Bookmark */}
                  <div className="flex items-center gap-1.5 shrink-0">
                    <button
                      onClick={() => handleTTS(msg.id, showTa && !showEn ? data.tamil_explanation : data.simple_explanation, showTa && !showEn ? 'ta' : 'en')}
                      className={`p-1.5 rounded-lg border text-xs flex items-center gap-1 transition-colors ${
                        isSpeaking
                          ? 'bg-cyan-500 text-slate-950 border-cyan-400 font-bold'
                          : 'bg-slate-900/80 text-slate-300 hover:text-cyan-300 border-slate-700/80'
                      }`}
                      title={isSpeaking ? 'Stop speaking' : 'Read aloud with text-to-speech'}
                    >
                      {isSpeaking ? <VolumeX className="w-3.5 h-3.5" /> : <Volume2 className="w-3.5 h-3.5" />}
                      <span className="hidden sm:inline">{isSpeaking ? 'Stop' : 'Listen'}</span>
                    </button>

                    <button
                      onClick={() => handleCopy(msg.id, data)}
                      className="p-1.5 rounded-lg bg-slate-900/80 text-slate-300 hover:text-white border border-slate-700/80 transition-colors"
                      title="Copy structured response"
                    >
                      {copiedId === msg.id ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                    </button>

                    {onSaveBookmark && (
                      <button
                        onClick={() => onSaveBookmark({ item_id: msg.id, item_type: 'chat_answer', title: data.question, data_json: JSON.stringify(data) })}
                        className={`p-1.5 rounded-lg border transition-colors ${
                          isSaved ? 'bg-amber-500/20 text-amber-300 border-amber-500/40' : 'bg-slate-900/80 text-slate-300 hover:text-amber-300 border-slate-700/80'
                        }`}
                        title="Save to bookmarks"
                      >
                        {isSaved ? <BookmarkCheck className="w-3.5 h-3.5" /> : <Bookmark className="w-3.5 h-3.5" />}
                      </button>
                    )}
                  </div>
                </div>

                {/* English Explanation */}
                {showEn && (
                  <div className="space-y-1.5">
                    <h4 className="text-xs font-bold text-cyan-300 uppercase tracking-wide flex items-center gap-1.5">
                      <Sparkles className="w-3.5 h-3.5" />
                      <span>Simple Explanation</span>
                    </h4>
                    <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
                      {data.simple_explanation}
                    </p>
                  </div>
                )}

                {/* What You Can Do (Action steps) */}
                {showEn && data.what_you_can_do && data.what_you_can_do.length > 0 && (
                  <div className="space-y-2 pt-1">
                    <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wide">
                      What You Can Do (உடனடி நடவடிக்கைகள்):
                    </h4>
                    <div className="space-y-1.5">
                      {data.what_you_can_do.map((step, idx) => (
                        <div
                          key={idx}
                          className="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800/80 flex items-start gap-2.5 text-xs text-slate-300 leading-relaxed"
                        >
                          <span className="w-5 h-5 rounded-full bg-cyan-500/20 text-brand-cyan flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">
                            {idx + 1}
                          </span>
                          <span>{step.replace(/^\d+\.\s*/, '')}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Your Rights */}
                {showEn && data.your_rights && data.your_rights.length > 0 && (
                  <div className="space-y-1.5 pt-1">
                    <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wide">
                      Your Statutory Rights (உங்கள் சட்ட உரிமைகள்):
                    </h4>
                    <ul className="space-y-1 text-xs text-slate-300 list-disc list-inside">
                      {data.your_rights.map((right, idx) => (
                        <li key={idx} className="leading-relaxed">
                          <span className="text-cyan-200">{right}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Where to Get Help */}
                {showEn && data.where_to_get_help && data.where_to_get_help.length > 0 && (
                  <div className="p-3 rounded-xl bg-blue-950/30 border border-blue-500/20 space-y-1.5">
                    <h4 className="text-xs font-bold text-blue-300 uppercase tracking-wide">
                      Where to Get Help (அணுக வேண்டிய துறைகள்):
                    </h4>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-xs text-slate-300">
                      {data.where_to_get_help.map((item, idx) => (
                        <div key={idx} className="flex items-center gap-1.5">
                          <ArrowRight className="w-3 h-3 text-brand-cyan shrink-0" />
                          <span>{item}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Tamil Explanation Section (தமிழ் விளக்கம்) */}
                {showTa && (
                  <div className="p-4 rounded-xl bg-slate-950/80 border border-purple-500/25 space-y-2 text-left">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-purple-500/20 text-purple-300 border border-purple-500/30 font-tamil">
                          தமிழ் விளக்கம்
                        </span>
                        <span className="text-xs font-bold text-white font-tamil">
                          எளிய தமிழ் வழிகாட்டுதல்
                        </span>
                      </div>
                      <button
                        onClick={() => handleTTS(`${msg.id}-ta`, data.tamil_explanation, 'ta')}
                        className="p-1 rounded text-slate-400 hover:text-purple-300"
                        title="Listen in Tamil"
                      >
                        <Volume2 className="w-3.5 h-3.5" />
                      </button>
                    </div>

                    <p className="text-xs sm:text-sm text-slate-200 leading-relaxed font-tamil">
                      {data.tamil_explanation}
                    </p>

                    {data.tamil_steps && data.tamil_steps.length > 0 && (
                      <div className="pt-2 space-y-1.5">
                        <span className="text-[11px] font-bold text-purple-300 font-tamil">
                          நீங்கள் செய்ய வேண்டியவை:
                        </span>
                        {data.tamil_steps.map((tStep, idx) => (
                          <div key={idx} className="text-xs text-slate-300 font-tamil flex items-start gap-2">
                            <span className="text-purple-400 font-bold shrink-0">•</span>
                            <span>{tStep}</span>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                )}

                {/* Verified Statutory Sources */}
                {data.sources && data.sources.length > 0 && (
                  <SourceCard sources={data.sources} />
                )}

                {/* Educational Disclaimer */}
                <div className="pt-2 text-[10px] sm:text-[11px] text-slate-400 italic flex items-start gap-1.5 border-t border-slate-800/60">
                  <Info className="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5" />
                  <span>{data.disclaimer}</span>
                </div>
              </div>
            </div>
          );
        })}

        {/* Loading Thinking State */}
        {loading && (
          <div className="flex justify-start">
            <div className="glass-card p-4 rounded-2xl rounded-tl-none border border-cyan-500/30 flex items-center gap-3 text-xs text-cyan-300">
              <Loader2 className="w-4 h-4 animate-spin text-brand-cyan" />
              <div className="space-y-1 text-left">
                <p className="font-semibold">NyaayaAI is analyzing Indian statutory provisions...</p>
                <p className="text-[10px] text-slate-400 font-tamil">சட்டப் பிரிவுகள் மற்றும் நடைமுறைகள் தொகுக்கப்படுகின்றன...</p>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Suggested Questions Pill bar */}
      <div className="py-2 overflow-x-auto whitespace-nowrap flex gap-2 no-scrollbar text-xs">
        {suggestedQuestions.map((sq, idx) => (
          <button
            key={idx}
            onClick={() => handleSend(sq.text)}
            className="px-3 py-1.5 rounded-full bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-cyan-500/30 text-slate-300 hover:text-white transition-all shrink-0 text-left"
          >
            <span className={sq.lang === 'ta' ? 'font-tamil text-cyan-300' : ''}>
              {sq.text}
            </span>
          </button>
        ))}
      </div>

      {/* Input Box Footer */}
      <div className="glass-panel p-2.5 rounded-2xl border border-cyan-500/20 shadow-glass">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSend();
          }}
          className="flex items-center gap-2"
        >
          {/* Voice Input Mic Button */}
          <button
            type="button"
            onClick={toggleRecording}
            className={`p-2.5 rounded-xl border transition-all ${
              isRecording
                ? 'bg-red-500 text-white border-red-400 animate-pulse shadow-glow-cyan'
                : 'bg-slate-900 text-slate-400 hover:text-cyan-300 border-slate-700/80'
            }`}
            title={isRecording ? 'Listening... click to stop' : 'Ask using voice (Speech-to-text)'}
          >
            {isRecording ? <MicOff className="w-4 h-4" /> : <Mic className="w-4 h-4" />}
          </button>

          {/* Text Input */}
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={
              currentLang === 'ta'
                ? "உங்கள் உரிமைகள், சட்டங்கள் அல்லது அரசு சேவைகள் பற்றி கேளுங்கள்..."
                : "Ask about your rights, laws, government services or complaints..."
            }
            className="flex-1 bg-transparent px-3 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none"
            disabled={loading}
          />

          {/* Send Button */}
          <button
            type="submit"
            disabled={!input.trim() || loading}
            className={`p-2.5 rounded-xl transition-all flex items-center justify-center ${
              input.trim() && !loading
                ? 'bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white shadow-glow-cyan scale-100'
                : 'bg-slate-800 text-slate-500 cursor-not-allowed'
            }`}
          >
            <Send className="w-4 h-4" />
          </button>
        </form>
      </div>
    </div>
  );
}
