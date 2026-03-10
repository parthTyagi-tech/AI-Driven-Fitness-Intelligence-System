import streamlit as st
import pandas as pd
import joblib
import random

# ------------------ Load model ------------------
model = joblib.load("gym_ai_bodyfat_model.pkl")

# ------------------ Page config + CSS ------------------
st.set_page_config(page_title="AI-Driven Fitness Intelligence System", layout="centered", page_icon="🏋️")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

/* ── GLOBAL RESET & THEME ────────────────────────────────── */
:root {
  --bg:        #0c0c0c;
  --surface:   #141414;
  --surface2:  #1c1c1c;
  --surface3:  #242424;
  --border:    rgba(255,255,255,0.08);
  --border2:   rgba(255,255,255,0.14);
  --accent:    #c8c8c8;
  --accent2:   #e8e8e8;
  --accent3:   #f0f0f0;
  --gold:      #b8a070;
  --gold2:     #d4b880;
  --red:       #cc4444;
  --text:      #e8e8e8;
  --muted:     rgba(220,220,220,0.45);
  --glow:      rgba(200,200,200,0.10);
  --glow2:     rgba(180,160,112,0.08);
  --glow3:     rgba(200,200,200,0.05);
}

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
  background-color: var(--bg) !important;
  color: var(--text) !important;
}

/* animated grain overlay */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: 0.5;
}

/* background grid lines */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.012) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.012) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
  z-index: 0;
}

/* ── STREAMLIT OVERRIDES ─────────────────────────────────── */
.stApp { background: var(--bg); }
.main .block-container {
  padding: 2rem 1.5rem 4rem;
  max-width: 820px;
  position: relative;
  z-index: 1;
}

/* hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── GYM HERO BANNER ─────────────────────────────────────── */
.gym-hero {
  position: relative;
  background: linear-gradient(135deg, #0c0c0c 0%, #1a1a1a 50%, #0c0c0c 100%);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 24px;
  padding: 40px 36px 32px;
  margin-bottom: 28px;
  overflow: hidden;
  animation: fadeSlideDown 0.6s cubic-bezier(.22,1,.36,1) both;
}
.gym-hero::before {
  content: '';
  position: absolute;
  top: -40px; right: -40px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(184,160,112,0.06) 0%, transparent 70%);
  border-radius: 50%;
}
.gym-hero::after {
  content: '';
  position: absolute;
  bottom: -30px; left: -30px;
  width: 160px; height: 160px;
  background: radial-gradient(circle, rgba(200,200,200,0.04) 0%, transparent 70%);
  border-radius: 50%;
}

/* floating dumbbell icons */
.gym-icons-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  animation: fadeSlideDown 0.5s ease both;
}
.gym-icon-badge {
  width: 36px; height: 36px;
  background: var(--surface2);
  border: 1px solid var(--border2);
  border-radius: 10px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  animation: floatBob 3s ease-in-out infinite;
}
.gym-icon-badge:nth-child(2) { animation-delay: 0.4s; }
.gym-icon-badge:nth-child(3) { animation-delay: 0.8s; }
.gym-icon-badge:nth-child(4) { animation-delay: 1.2s; }
.gym-icon-badge:nth-child(5) { animation-delay: 1.6s; }

/* ── TITLE ───────────────────────────────────────────────── */
.hero-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3.2rem, 8vw, 5.5rem);
  letter-spacing: 0.06em;
  line-height: 1;
  color: var(--accent3);
  margin: 0;
  animation: fadeSlideDown 0.7s cubic-bezier(.22,1,.36,1) both;
  text-shadow: 0 0 60px rgba(255,255,255,0.05);
}
.hero-title .accent-word {
  background: linear-gradient(135deg, var(--gold) 0%, var(--gold2) 60%, #f0e8d0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-sub {
  font-size: 0.78rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  margin-top: 0.5rem;
  font-family: 'Space Mono', monospace;
  animation: fadeSlideDown 0.9s cubic-bezier(.22,1,.36,1) both;
}

/* ── MOTIVATIONAL QUOTE CARD ──────────────────────────────── */
.quote-card {
  background: linear-gradient(135deg, var(--surface) 0%, var(--surface2) 100%);
  border: 1px solid rgba(184,160,112,0.2);
  border-left: 3px solid var(--gold);
  border-radius: 14px;
  padding: 18px 22px;
  margin: 20px 0 24px;
  position: relative;
  overflow: hidden;
  animation: fadeSlideUp 0.8s cubic-bezier(.22,1,.36,1) 0.3s both;
}
.quote-card::before {
  content: '"';
  position: absolute;
  top: -10px; left: 10px;
  font-size: 5rem;
  font-family: 'Bebas Neue', sans-serif;
  color: rgba(184,160,112,0.08);
  line-height: 1;
  pointer-events: none;
}
.quote-text {
  font-size: 0.9rem;
  font-style: italic;
  color: var(--accent2);
  letter-spacing: 0.03em;
  line-height: 1.6;
  margin: 0;
}
.quote-author {
  font-family: 'Space Mono', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold);
  margin-top: 8px;
}

/* ── STATS BAR ────────────────────────────────────────────── */
.stats-bar {
  display: flex;
  gap: 1px;
  background: var(--border);
  border-radius: 14px;
  overflow: hidden;
  margin-bottom: 24px;
  animation: fadeSlideUp 0.6s ease 0.2s both;
}
.stat-item {
  flex: 1;
  background: var(--surface);
  padding: 14px 12px;
  text-align: center;
  transition: background 0.2s;
}
.stat-item:hover { background: var(--surface2); }
.stat-num {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.5rem;
  letter-spacing: 0.04em;
  color: var(--gold2);
  line-height: 1;
}
.stat-lbl {
  font-family: 'Space Mono', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  margin-top: 4px;
}

/* ── PROGRESS BAR ────────────────────────────────────────── */
.stProgress > div > div > div {
  background: linear-gradient(90deg, #555, var(--accent2)) !important;
  border-radius: 99px !important;
  transition: width 0.6s cubic-bezier(.22,1,.36,1) !important;
  box-shadow: 0 0 8px rgba(200,200,200,0.15) !important;
}
.stProgress > div > div {
  background: var(--surface2) !important;
  border-radius: 99px !important;
  height: 4px !important;
}

/* ── STEP BADGE ──────────────────────────────────────────── */
.step-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 6px 18px 6px 6px;
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 99px;
  margin-bottom: 1.4rem;
  animation: fadeSlideDown 0.5s ease both;
}
.step-badge .dot {
  width: 28px; height: 28px;
  border-radius: 50%;
  background: linear-gradient(135deg, #555, #999);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Space Mono', monospace;
  font-size: 0.75rem;
  font-weight: 700;
  color: #f0f0f0;
  box-shadow: 0 0 12px rgba(150,150,150,0.2);
}
.step-badge .label {
  font-size: 0.78rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  font-family: 'Space Mono', monospace;
}

/* ── CARD ────────────────────────────────────────────────── */
.fx-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 28px 24px;
  margin-bottom: 18px;
  position: relative;
  overflow: hidden;
  animation: fadeSlideUp 0.55s cubic-bezier(.22,1,.36,1) both;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.fx-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at top left, rgba(184,160,112,0.03), transparent 65%);
  pointer-events: none;
  border-radius: 20px;
}
.fx-card:hover {
  border-color: rgba(255,255,255,0.12);
  box-shadow: 0 0 40px rgba(255,255,255,0.03);
}

.fx-card-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.5rem;
  letter-spacing: 0.08em;
  color: var(--accent3);
  margin-bottom: 1.2rem;
  display: flex;
  align-items: center;
  gap: 10px;
}

/* ── SECTION LABEL ───────────────────────────────────────── */
.sec-label {
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  font-family: 'Space Mono', monospace;
  margin-bottom: 0.6rem;
  display: block;
}

/* ── INPUTS ──────────────────────────────────────────────── */
div[data-baseweb="input"] input,
div[data-baseweb="select"] div[data-baseweb="select"],
div[data-baseweb="base-input"] input,
.stSelectbox div[data-baseweb="select"] > div,
.stNumberInput input,
.stTextInput input {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  color: var(--text) !important;
  font-family: 'DM Sans', sans-serif !important;
  transition: border-color 0.25s, box-shadow 0.25s !important;
}
div[data-baseweb="input"]:focus-within input,
.stNumberInput:focus-within input {
  border-color: rgba(200,200,200,0.4) !important;
  box-shadow: 0 0 0 3px rgba(200,200,200,0.07) !important;
}

/* dropdown */
[data-baseweb="popover"] {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
}
[data-baseweb="menu"] {
  background: var(--surface2) !important;
}
[role="option"] {
  background: var(--surface2) !important;
  color: var(--text) !important;
}
[role="option"]:hover {
  background: var(--surface3) !important;
  color: var(--accent3) !important;
}

/* labels */
.stSelectbox label, .stNumberInput label, .stSlider label,
.stTextInput label {
  color: var(--muted) !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.08em !important;
  font-family: 'Space Mono', monospace !important;
  text-transform: uppercase !important;
}

/* slider */
.stSlider > div > div > div > div {
  background: linear-gradient(90deg, #444, #999) !important;
  box-shadow: 0 0 8px rgba(180,180,180,0.12) !important;
}
.stSlider > div > div > div {
  background: var(--surface2) !important;
}
.stSlider > div > div > div > div > div {
  background: #e0e0e0 !important;
  border: 2px solid var(--bg) !important;
  box-shadow: 0 0 12px rgba(200,200,200,0.2) !important;
  width: 20px !important;
  height: 20px !important;
}

/* ── BUTTONS ─────────────────────────────────────────────── */
.stButton > button {
  background: transparent !important;
  border: 1px solid var(--border2) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  padding: 0.65rem 1.4rem !important;
  font-family: 'Space Mono', monospace !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  transition: all 0.25s cubic-bezier(.22,1,.36,1) !important;
  position: relative;
  overflow: hidden;
}
.stButton > button:hover {
  border-color: rgba(255,255,255,0.35) !important;
  color: var(--accent3) !important;
  box-shadow: 0 0 24px rgba(200,200,200,0.08), inset 0 0 24px rgba(255,255,255,0.02) !important;
  transform: translateY(-1px) !important;
}
.stButton > button:active {
  transform: translateY(0) !important;
}

/* primary CTA */
.cta-btn > div > button,
.cta-btn .stButton > button {
  background: linear-gradient(135deg, #333 0%, #555 50%, #777 100%) !important;
  color: #f0f0f0 !important;
  border: 1px solid rgba(255,255,255,0.15) !important;
  font-weight: 700 !important;
  font-size: 0.85rem !important;
  box-shadow: 0 4px 24px rgba(0,0,0,0.4) !important;
}
.cta-btn > div > button:hover,
.cta-btn .stButton > button:hover {
  background: linear-gradient(135deg, #444 0%, #666 50%, #888 100%) !important;
  box-shadow: 0 6px 32px rgba(200,200,200,0.1), 0 0 0 1px rgba(255,255,255,0.2) !important;
  transform: translateY(-2px) !important;
  color: #ffffff !important;
}

/* ── METRIC ──────────────────────────────────────────────── */
[data-testid="stMetric"] {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 16px !important;
  padding: 20px !important;
  text-align: center !important;
  position: relative;
  overflow: hidden;
  animation: scaleIn 0.5s cubic-bezier(.22,1,.36,1) both;
}
[data-testid="stMetric"]::before {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, #333, #888, #333);
  border-radius: 0 0 16px 16px;
}
[data-testid="stMetricLabel"] {
  color: var(--muted) !important;
  font-family: 'Space Mono', monospace !important;
  font-size: 0.7rem !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
  font-family: 'Bebas Neue', sans-serif !important;
  font-size: 2.8rem !important;
  letter-spacing: 0.04em !important;
  color: var(--accent3) !important;
}

/* ── SUCCESS / INFO ALERTS ───────────────────────────────── */
.stSuccess {
  background: rgba(80,160,80,0.07) !important;
  border: 1px solid rgba(80,160,80,0.2) !important;
  border-radius: 12px !important;
  color: #90cc90 !important;
}
.stInfo {
  background: rgba(200,200,200,0.04) !important;
  border: 1px solid rgba(200,200,200,0.1) !important;
  border-radius: 12px !important;
}

/* ── EXPANDER ────────────────────────────────────────────── */
.streamlit-expanderHeader {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  font-family: 'Space Mono', monospace !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.08em !important;
  color: var(--muted) !important;
  padding: 14px 18px !important;
  transition: all 0.25s !important;
}
.streamlit-expanderHeader:hover {
  border-color: rgba(255,255,255,0.25) !important;
  color: var(--accent3) !important;
}
.streamlit-expanderContent {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-top: none !important;
  border-radius: 0 0 12px 12px !important;
  padding: 16px 20px !important;
}

/* ── EXERCISE ITEM ───────────────────────────────────────── */
.ex-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 14px;
  margin-bottom: 6px;
  background: var(--surface2);
  border-radius: 10px;
  border: 1px solid var(--border);
  transition: all 0.2s;
  animation: fadeSlideUp 0.4s ease both;
}
.ex-item:hover {
  border-color: rgba(255,255,255,0.15);
  transform: translateX(4px);
  background: var(--surface3);
}
.ex-name {
  font-size: 0.88rem;
  color: var(--text);
}
.ex-reps {
  font-family: 'Space Mono', monospace;
  font-size: 0.75rem;
  color: var(--accent2);
  background: rgba(255,255,255,0.05);
  padding: 3px 10px;
  border-radius: 99px;
  border: 1px solid rgba(255,255,255,0.1);
}

/* ── SPLIT TAG ───────────────────────────────────────────── */
.split-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 12px 0 20px;
}
.split-tag {
  padding: 5px 14px;
  background: var(--surface2);
  border: 1px solid var(--border2);
  border-radius: 99px;
  font-family: 'Space Mono', monospace;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  animation: fadeSlideDown 0.4s ease both;
  transition: all 0.2s;
}
.split-tag:hover {
  border-color: rgba(255,255,255,0.25);
  color: var(--accent3);
}

/* ── WORKOUT TYPE CARDS ──────────────────────────────────── */
.wt-card {
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 32px 24px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(.22,1,.36,1);
  background: var(--surface);
  position: relative;
  overflow: hidden;
  animation: fadeSlideUp 0.5s ease both;
}
.wt-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(255,255,255,0.03), transparent 70%);
  opacity: 0;
  transition: opacity 0.3s;
}
.wt-card:hover { border-color: rgba(255,255,255,0.25); box-shadow: 0 0 40px rgba(200,200,200,0.06); }
.wt-card:hover::before { opacity: 1; }
.wt-icon { font-size: 2.8rem; display: block; margin-bottom: 12px; animation: floatBob 3s ease-in-out infinite; }
.wt-label {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.6rem;
  letter-spacing: 0.06em;
  color: var(--text);
}
.wt-sub { font-size: 0.78rem; color: var(--muted); margin-top: 6px; }

/* ── RESULT BADGE ────────────────────────────────────────── */
.result-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  border-radius: 99px;
  font-family: 'Space Mono', monospace;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  border: 1px solid;
  margin-top: 10px;
  animation: scaleIn 0.6s cubic-bezier(.22,1,.36,1) 0.3s both;
}
.badge-healthy  { background: rgba(80,160,80,0.08);   border-color: rgba(80,160,80,0.3);   color: #90cc90; }
.badge-lower    { background: rgba(200,200,200,0.06);  border-color: rgba(200,200,200,0.2);  color: var(--accent2); }
.badge-higher   { background: rgba(200,160,60,0.08);   border-color: rgba(200,160,60,0.3);   color: var(--gold2); }
.badge-high     { background: rgba(180,60,60,0.08);    border-color: rgba(180,60,60,0.3);    color: #cc7070; }

/* ── DIVIDER ─────────────────────────────────────────────── */
.fx-divider {
  height: 1px;
  background: var(--border);
  margin: 20px 0;
}

/* ── SMALL NOTE ──────────────────────────────────────────── */
.small-note {
  font-size: 0.75rem;
  color: var(--muted);
  font-family: 'Space Mono', monospace;
  letter-spacing: 0.05em;
}

/* ── MOTIVATIONAL TICKER ─────────────────────────────────── */
.ticker-wrap {
  overflow: hidden;
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 10px 0;
  margin: 20px 0;
}
.ticker-text {
  font-family: 'Space Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gold);
  white-space: nowrap;
  animation: tickerScroll 22s linear infinite;
  display: inline-block;
  padding-left: 100%;
}
@keyframes tickerScroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-100%); }
}

/* ── GYM SYMBOL ROW ──────────────────────────────────────── */
.symbol-row {
  display: flex;
  justify-content: center;
  gap: 24px;
  padding: 20px 0 8px;
  animation: fadeSlideUp 1s ease 0.5s both;
}
.sym {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  opacity: 0.6;
  transition: opacity 0.3s, transform 0.3s;
  cursor: default;
}
.sym:hover { opacity: 1; transform: translateY(-3px); }
.sym-icon { font-size: 1.6rem; }
.sym-text {
  font-family: 'Space Mono', monospace;
  font-size: 0.55rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

/* ── RESULT ANALYSIS CARD ─────────────────────────────────── */
.analysis-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin: 16px 0;
}
.analysis-item {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 16px;
  animation: fadeSlideUp 0.5s ease both;
  transition: border-color 0.2s;
}
.analysis-item:hover { border-color: rgba(255,255,255,0.16); }
.analysis-label {
  font-family: 'Space Mono', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
}
.analysis-value {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.3rem;
  letter-spacing: 0.04em;
  color: var(--accent3);
}

/* ── KEYFRAMES ───────────────────────────────────────────── */
@keyframes fadeSlideDown {
  from { opacity: 0; transform: translateY(-16px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.92); }
  to   { opacity: 1; transform: scale(1); }
}
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 20px rgba(200,200,200,0.08); }
  50%       { box-shadow: 0 0 40px rgba(200,200,200,0.14), 0 0 80px rgba(200,200,200,0.06); }
}
@keyframes floatBob {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-6px); }
}
@keyframes shimmer {
  0%   { background-position: -200% center; }
  100% { background-position: 200% center; }
}

/* ── OPTIONAL FIELD BOX ──────────────────────────────────── */
.opt-box {
  background: var(--surface2);
  border: 1px dashed rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 18px;
  margin: 16px 0;
}
.opt-title {
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
  font-family: 'Space Mono', monospace;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.opt-title span {
  width: 16px; height: 1px;
  background: var(--border);
  display: inline-block;
}

/* ── SPINNER ─────────────────────────────────────────────── */
.stSpinner > div {
  border-top-color: var(--accent) !important;
}

/* columns gap */
[data-testid="column"] { gap: 12px; }

/* ── LOGO BADGE TOP RIGHT ─────────────────────────────────── */
.brand-badge {
  position: absolute;
  top: 24px; right: 28px;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px;
  padding: 6px 12px;
  font-family: 'Space Mono', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--gold);
  animation: fadeSlideDown 1s ease 0.4s both;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Motivational Quotes ------------------
GYM_QUOTES = [
    ("The only bad workout is the one that didn't happen.", "Unknown"),
    ("Train insane or remain the same.", "Jadah Sellner"),
    ("Your body can stand almost anything. It's your mind you have to convince.", "Unknown"),
    ("No pain, no gain. Shut up and train.", "Unknown"),
    ("Strength doesn't come from what you can do. It comes from overcoming what you thought you couldn't.", "Rikki Rogers"),
    ("The iron never lies to you.", "Henry Rollins"),
    ("Push yourself because no one else is going to do it for you.", "Unknown"),
    ("Fall in love with taking care of yourself.", "Unknown"),
    ("Discipline is the bridge between goals and accomplishment.", "Jim Rohn"),
    ("Every rep, every set, every drop of sweat — it all adds up.", "Unknown"),
    ("Wake up. Work out. Look hot. Kick ass.", "Unknown"),
    ("Hustle for that muscle.", "Unknown"),
    ("Be stronger than your excuses.", "Unknown"),
    ("The gym is my therapy. Iron is my medicine.", "Unknown"),
    ("It never gets easier. You just get stronger.", "Unknown"),
]

# ------------------ Session State (wizard steps) ------------------
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_df" not in st.session_state:
    st.session_state.user_df = None
if "pred_bf" not in st.session_state:
    st.session_state.pred_bf = None
if "bf_cat" not in st.session_state:
    st.session_state.bf_cat = None
if "quote_idx" not in st.session_state:
    st.session_state.quote_idx = random.randint(0, len(GYM_QUOTES) - 1)

# ------------------ Helper: BF category ------------------
def bf_category(bf, gender=None):
    g = str(gender).lower().strip() if gender is not None else None
    if bf is None:
        return "unknown"
    if g not in ["male", "female"]:
        if bf < 12: return "lower"
        if bf < 20: return "healthy"
        if bf < 28: return "higher"
        return "high"
    if g == "male":
        if bf < 10: return "lower"
        if bf < 20: return "healthy"
        if bf < 25: return "higher"
        return "high"
    else:
        if bf < 18: return "lower"
        if bf < 28: return "healthy"
        if bf < 33: return "higher"
        return "high"

# ------------------ HOME EXERCISES ------------------
HOME_EXERCISES = {
    "Full Body A": {
        "no_equipment": [
            ("Squats", "3x12"), ("Push-ups", "3x8-12"),
            ("Glute Bridge", "3x15"), ("Plank", "3x30-45s")
        ],
        "minimal": [
            ("Backpack Squat", "3x10-12"), ("Push-ups", "3x8-12"),
            ("Backpack Row", "3x10-12"), ("Plank", "3x30-60s")
        ]
    },
    "Upper": {
        "no_equipment": [
            ("Push-ups", "4x8-12"), ("Chair Dips", "3x8-12"),
            ("Pike Push-ups", "3x6-10")
        ],
        "minimal": [
            ("Backpack Row", "4x10-12"), ("Overhead Press", "3x10-12"),
            ("Bicep Curl (bags)", "3x12-15")
        ]
    },
    "Lower": {
        "no_equipment": [
            ("Squats", "4x12-15"), ("Reverse Lunges", "3x10/leg"),
            ("Glute Bridge", "4x15")
        ],
        "minimal": [
            ("Backpack Squat", "4x10-12"), ("Bulgarian Split Squat", "3x8-10/leg"),
            ("Backpack RDL", "4x10-12")
        ]
    }
}

# ------------------ GYM EXERCISES ------------------
GYM_EXERCISES = {
    "Upper": [
        ("Bench Press", "4x6-10"), ("Lat Pulldown / Pull-ups", "4x8-12"),
        ("Overhead Shoulder Press", "3x8-12"), ("Seated Row", "3x10-12"),
        ("Bicep Curls", "3x12-15"), ("Tricep Pushdown", "3x12-15")
    ],
    "Lower": [
        ("Barbell Squat", "4x6-10"), ("Leg Press", "3x10-12"),
        ("Romanian Deadlift", "3x8-12"), ("Leg Curl", "3x12-15"),
        ("Calf Raises", "4x15-20")
    ],
    "Full Body A": [
        ("Squat", "4x6-10"), ("Bench Press", "3x8-12"),
        ("Lat Pulldown", "3x10-12"), ("Shoulder Press", "3x10-12"),
        ("Plank", "3x45s")
    ],
    "Push": [
        ("Bench Press", "4x6-10"), ("Incline Dumbbell Press", "3x8-12"),
        ("Shoulder Press", "3x8-12"), ("Lateral Raises", "3x12-15"),
        ("Tricep Pushdown", "3x12-15")
    ],
    "Pull": [
        ("Deadlift", "3x5-8"), ("Lat Pulldown", "4x8-12"),
        ("Seated Row", "3x10-12"), ("Face Pull", "3x12-15"),
        ("Bicep Curls", "3x12-15")
    ],
    "Legs": [
        ("Squats", "4x6-10"), ("Leg Press", "3x10-12"),
        ("Romanian Deadlift", "3x8-12"), ("Leg Curl", "3x12-15"),
        ("Calf Raises", "4x15-20")
    ]
}

# ------------------ Split functions ------------------
def choose_split(workouts_per_week: int):
    if workouts_per_week <= 1: return ["Full Body A"]
    if workouts_per_week == 2: return ["Full Body A", "Full Body B"]
    if workouts_per_week == 3: return ["Upper", "Lower", "Full Body A"]
    if workouts_per_week == 4: return ["Upper", "Lower", "Upper", "Lower"]
    if workouts_per_week == 5: return ["Push", "Pull", "Legs", "Upper", "Lower"]
    return ["Push", "Pull", "Legs", "Push", "Pull", "Legs"]

def home_workout_plan(workouts_per_week: int, equipment: str = "no_equipment"):
    split = choose_split(workouts_per_week)
    plan = {}
    for i, day in enumerate(split, start=1):
        plan[f"Day {i} - {day}"] = HOME_EXERCISES[day][equipment]
    return split, plan

# ── HERO SECTION ────────────────────────────────────────────────────
st.markdown("""
<div class="gym-hero">
  <div class="brand-badge">⚡ AI POWERED</div>
  <div class="gym-icons-row">
    <div class="gym-icon-badge">🏋️</div>
    <div class="gym-icon-badge">💪</div>
    <div class="gym-icon-badge">🔥</div>
    <div class="gym-icon-badge">⚡</div>
    <div class="gym-icon-badge">🎯</div>
  </div>
  <h1 class="hero-title">AI <span class="accent-word">FITNESS</span> COACH</h1>
  <p class="hero-sub">Personalized · Data-Driven · Precision Training</p>
  <div class="symbol-row">
    <div class="sym"><span class="sym-icon">🏋️</span><span class="sym-text">Strength</span></div>
    <div class="sym"><span class="sym-icon">🧬</span><span class="sym-text">Analytics</span></div>
    <div class="sym"><span class="sym-icon">🔬</span><span class="sym-text">Science</span></div>
    <div class="sym"><span class="sym-icon">📊</span><span class="sym-text">Tracking</span></div>
    <div class="sym"><span class="sym-icon">🏆</span><span class="sym-text">Results</span></div>
    <div class="sym"><span class="sym-icon">⚡</span><span class="sym-text">Power</span></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STATS BAR ─────────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
  <div class="stat-item"><div class="stat-num">10K+</div><div class="stat-lbl">Athletes</div></div>
  <div class="stat-item"><div class="stat-num">98%</div><div class="stat-lbl">Accuracy</div></div>
  <div class="stat-item"><div class="stat-num">4</div><div class="stat-lbl">Step Process</div></div>
  <div class="stat-item"><div class="stat-num">AI</div><div class="stat-lbl">Powered</div></div>
</div>
""", unsafe_allow_html=True)

# ── MOTIVATIONAL QUOTE ─────────────────────────────────────────────
q_text, q_author = GYM_QUOTES[st.session_state.quote_idx]
st.markdown(f"""
<div class="quote-card">
  <p class="quote-text">{q_text}</p>
  <div class="quote-author">— {q_author}</div>
</div>
""", unsafe_allow_html=True)

# ── SCROLLING TICKER ───────────────────────────────────────────────
st.markdown("""
<div class="ticker-wrap">
  <span class="ticker-text">
    🏋️ TRAIN HARD &nbsp;&nbsp;•&nbsp;&nbsp; 💪 STAY CONSISTENT &nbsp;&nbsp;•&nbsp;&nbsp; 🔥 BURN FAT &nbsp;&nbsp;•&nbsp;&nbsp;
    ⚡ BUILD MUSCLE &nbsp;&nbsp;•&nbsp;&nbsp; 🎯 HIT YOUR GOALS &nbsp;&nbsp;•&nbsp;&nbsp; 🏆 BE UNSTOPPABLE &nbsp;&nbsp;•&nbsp;&nbsp;
    🧬 AI PRECISION &nbsp;&nbsp;•&nbsp;&nbsp; 📊 DATA-DRIVEN &nbsp;&nbsp;•&nbsp;&nbsp; 🔬 SCIENCE-BACKED &nbsp;&nbsp;•&nbsp;&nbsp;
    🏋️ TRAIN HARD &nbsp;&nbsp;•&nbsp;&nbsp; 💪 STAY CONSISTENT &nbsp;&nbsp;•&nbsp;&nbsp; 🔥 BURN FAT &nbsp;&nbsp;•&nbsp;&nbsp;
    ⚡ BUILD MUSCLE &nbsp;&nbsp;•&nbsp;&nbsp; 🎯 HIT YOUR GOALS &nbsp;&nbsp;•&nbsp;&nbsp; 🏆 BE UNSTOPPABLE
  </span>
</div>
""", unsafe_allow_html=True)

# ── PROGRESS BAR ─────────────────────────────────────────────────
progress_map = {1: 0.20, 2: 0.50, 3: 0.75, 4: 1.00}
st.progress(progress_map.get(st.session_state.step, 0.20))

STEP_LABELS = {
    1: "Your Details",
    2: "AI Prediction",
    3: "Workout Type",
    4: "Your Plan",
}
step = st.session_state.step
st.markdown(f"""
<div class="step-badge">
  <div class="dot">{step}</div>
  <span class="label">Step {step} of 4 — {STEP_LABELS.get(step,'')}</span>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# STEP 1 — User Details
# ═══════════════════════════════════════════════════════════════════
if st.session_state.step == 1:
    st.markdown('<div class="fx-card">', unsafe_allow_html=True)
    st.markdown('<div class="fx-card-title">🏋️ ENTER YOUR DETAILS</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=10, max_value=80, value=22)
        gender = st.selectbox("Gender", ["male", "female"])
        activity_level = st.selectbox("Activity Level", ["sedentary", "light", "moderate", "active"])
    with col2:
        height_cm = st.number_input("Height (cm)", min_value=120.0, max_value=230.0, value=170.0)
        weight_kg = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
        workouts_per_week = st.slider("Workouts / Week", 0, 6, 3)

    st.markdown('<div class="fx-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="opt-box">', unsafe_allow_html=True)
    st.markdown('<div class="opt-title"><span></span> Optional — improves accuracy <span></span></div>', unsafe_allow_html=True)

    c3, c4, c5 = st.columns(3)
    with c3:
        waist_cm = st.number_input("Waist (cm)", min_value=40.0, max_value=200.0, value=80.0)
    with c4:
        neck_cm = st.number_input("Neck (cm)", min_value=20.0, max_value=80.0, value=36.0)
    with c5:
        hip_cm = st.number_input("Hip (cm)", min_value=40.0, max_value=200.0, value=95.0)
    st.markdown('</div>', unsafe_allow_html=True)

    sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
    daily_calories = st.number_input("Daily Calories (approx)", min_value=800, max_value=5000, value=2200)
    fitness_goal = st.selectbox("Fitness Goal", ["fat_loss", "maintain", "muscle_gain"])

    st.markdown('<p class="small-note">💡 Tip: Measurements like waist, neck & hip significantly improve prediction accuracy.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Motivational note before CTA
    st.markdown("""
    <div style="text-align:center; padding: 12px 0 6px; font-family:'Space Mono',monospace;
         font-size:0.68rem; letter-spacing:0.16em; color:rgba(220,200,140,0.5); text-transform:uppercase;">
      ⚡ Your transformation starts with one click ⚡
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="cta-btn">', unsafe_allow_html=True)
    if st.button("🔬 Predict My Body Fat →", use_container_width=True):
        user_df = pd.DataFrame([{
            "age": age, "gender": gender, "height_cm": height_cm,
            "weight_kg": weight_kg, "waist_cm": waist_cm, "neck_cm": neck_cm,
            "hip_cm": hip_cm, "sleep_hours": sleep_hours,
            "workouts_per_week": workouts_per_week, "daily_calories": daily_calories,
            "activity_level": activity_level, "fitness_goal": fitness_goal
        }])
        user_df["fitness_goal"] = user_df["fitness_goal"].astype(str).str.lower().str.strip().str.replace(" ", "_")
        user_df["activity_level"] = user_df["activity_level"].astype(str).str.lower().str.strip()
        user_df["gender"] = user_df["gender"].astype(str).str.lower().str.strip()
        st.session_state.user_df = user_df
        st.session_state.quote_idx = random.randint(0, len(GYM_QUOTES) - 1)
        st.session_state.step = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# STEP 2 — Predict
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.step == 2:
    st.markdown('<div class="fx-card">', unsafe_allow_html=True)
    st.markdown('<div class="fx-card-title">🧬 AI BODY FAT PREDICTION</div>', unsafe_allow_html=True)
    st.markdown('<p class="small-note">Running our trained model on your data…</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    with st.spinner("⚡ Analysing your data…"):
        pred_bf = float(model.predict(st.session_state.user_df)[0])

    gender_val = st.session_state.user_df.loc[0, "gender"]
    cat = bf_category(pred_bf, gender_val)
    st.session_state.pred_bf = pred_bf
    st.session_state.bf_cat = cat

    st.success("✅ Prediction complete — your results are ready!")

    st.metric("Predicted Body Fat %", f"{pred_bf:.2f}%")

    badge_map = {
        "healthy": ("badge-healthy", "● Healthy Range"),
        "lower":   ("badge-lower",   "▼ Below Range"),
        "higher":  ("badge-higher",  "▲ Above Range"),
        "high":    ("badge-high",    "⚠ High — Take Action"),
    }
    bcls, blabel = badge_map.get(cat, ("badge-lower", cat))
    st.markdown(f'<div class="result-badge {bcls}">{blabel}</div>', unsafe_allow_html=True)

    # Analysis grid
    u = st.session_state.user_df.loc[0]
    bmi = round(float(u["weight_kg"]) / ((float(u["height_cm"]) / 100) ** 2), 1)
    st.markdown(f"""
    <div class="analysis-grid" style="margin-top:20px;">
      <div class="analysis-item">
        <div class="analysis-label">💪 Body Fat</div>
        <div class="analysis-value">{pred_bf:.1f}%</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-label">⚖️ BMI Estimate</div>
        <div class="analysis-value">{bmi}</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-label">🏃 Activity Level</div>
        <div class="analysis-value" style="font-size:1rem;text-transform:capitalize;">{u['activity_level']}</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-label">🎯 Fitness Goal</div>
        <div class="analysis-value" style="font-size:1rem;text-transform:capitalize;">{str(u['fitness_goal']).replace('_',' ')}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if cat == "healthy":
        st.balloons()
        st.markdown("""
        <div style="text-align:center; padding:12px; font-family:'Space Mono',monospace;
             font-size:0.72rem; color:rgba(144,204,144,0.8); letter-spacing:0.1em;">
          🏆 YOU'RE IN THE HEALTHY RANGE — KEEP CRUSHING IT! 🏆
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("← Back", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    with c2:
        st.markdown('<div class="cta-btn">', unsafe_allow_html=True)
        if st.button("Choose Workout →", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# STEP 3 — Home vs Gym
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.step == 3:
    st.markdown('<div class="fx-card">', unsafe_allow_html=True)
    st.markdown('<div class="fx-card-title">⚡ WHERE DO YOU TRAIN?</div>', unsafe_allow_html=True)
    st.markdown('<p class="small-note">We\'ll build a personalised plan based on your environment.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    b1, b2 = st.columns(2)
    with b1:
        st.markdown("""
        <div class="wt-card">
          <span class="wt-icon">🏠</span>
          <div class="wt-label">Home</div>
          <div class="wt-sub">No gym required</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Home", use_container_width=True, key="home_btn"):
            st.session_state.workout_type = "home"
            st.session_state.step = 4
            st.rerun()

    with b2:
        st.markdown("""
        <div class="wt-card">
          <span class="wt-icon">🏋️</span>
          <div class="wt-label">Gym</div>
          <div class="wt-sub">Full equipment access</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Gym", use_container_width=True, key="gym_btn"):
            st.session_state.workout_type = "gym"
            st.session_state.step = 4
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# ═══════════════════════════════════════════════════════════════════
# STEP 4 — Plan
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.step == 4:
    user_df = st.session_state.user_df
    w = int(user_df.loc[0, "workouts_per_week"])
    goal = user_df.loc[0, "fitness_goal"]
    act = user_df.loc[0, "activity_level"]
    gender_val = user_df.loc[0, "gender"]
    pred_bf = float(st.session_state.pred_bf)
    cat = st.session_state.bf_cat

    # Summary strip
    st.markdown(f"""
    <div class="fx-card" style="padding:18px 24px; display:flex; flex-wrap:wrap; gap:20px;">
      <div>
        <span class="sec-label">🔬 Body Fat</span>
        <span style="font-family:'Bebas Neue',sans-serif; font-size:1.6rem; color:var(--accent3);">{pred_bf:.2f}%</span>
      </div>
      <div>
        <span class="sec-label">📊 Category</span>
        <span style="font-size:0.88rem; text-transform:capitalize;">{cat}</span>
      </div>
      <div>
        <span class="sec-label">🎯 Goal</span>
        <span style="font-size:0.88rem; text-transform:capitalize;">{goal.replace('_',' ')}</span>
      </div>
      <div>
        <span class="sec-label">⚡ Activity</span>
        <span style="font-size:0.88rem; text-transform:capitalize;">{act}</span>
      </div>
      <div>
        <span class="sec-label">📍 Mode</span>
        <span style="font-size:0.88rem; text-transform:capitalize;">{'🏠 Home' if st.session_state.get('workout_type')=='home' else '🏋️ Gym'}</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Motivational quote for plan step
    plan_quotes = [
        "💪 Today's workout is tomorrow's strength.",
        "🔥 Every set is a step closer to your goal.",
        "⚡ Consistency beats intensity every single time.",
        "🏆 Champions are made in the gym, revealed everywhere else.",
    ]
    st.markdown(f"""
    <div style="text-align:center; padding: 8px 0 16px; font-family:'Space Mono',monospace;
         font-size:0.7rem; letter-spacing:0.12em; color:rgba(220,200,140,0.6); text-transform:uppercase;">
      {random.choice(plan_quotes)}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="fx-card">', unsafe_allow_html=True)

    if st.session_state.get("workout_type") == "home":
        st.markdown('<div class="fx-card-title">🏠 HOME WORKOUT PLAN</div>', unsafe_allow_html=True)
        equipment = st.selectbox("Equipment available", ["no_equipment", "minimal"], index=0)
        st.markdown('<div class="fx-divider"></div>', unsafe_allow_html=True)

        split, plan = home_workout_plan(w, equipment=equipment)

        st.markdown('<span class="sec-label">Weekly Split</span>', unsafe_allow_html=True)
        tags_html = ''.join([f'<span class="split-tag">{s}</span>' for s in split])
        st.markdown(f'<div class="split-tags">{tags_html}</div>', unsafe_allow_html=True)

        st.markdown('<span class="sec-label">Exercise Breakdown</span>', unsafe_allow_html=True)
        for day, exercises in plan.items():
            with st.expander(f"📅  {day}"):
                for ex, reps in exercises:
                    st.markdown(f"""
                    <div class="ex-item">
                      <span class="ex-name">💪 {ex}</span>
                      <span class="ex-reps">{reps}</span>
                    </div>
                    """, unsafe_allow_html=True)

    else:
        st.markdown('<div class="fx-card-title">🏋️ GYM WORKOUT PLAN</div>', unsafe_allow_html=True)

        split = choose_split(w)

        st.markdown('<span class="sec-label">Weekly Split</span>', unsafe_allow_html=True)
        tags_html = ''.join([f'<span class="split-tag">{s}</span>' for s in split])
        st.markdown(f'<div class="split-tags">{tags_html}</div>', unsafe_allow_html=True)

        st.markdown('<span class="sec-label">Exercise Breakdown</span>', unsafe_allow_html=True)
        for i, day in enumerate(split, start=1):
            exercises = GYM_EXERCISES.get(day, [])
            with st.expander(f"📅  Day {i} — {day}"):
                for ex, reps in exercises:
                    st.markdown(f"""
                    <div class="ex-item">
                      <span class="ex-name">🔥 {ex}</span>
                      <span class="ex-reps">{reps}</span>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer motivation
    st.markdown("""
    <div style="text-align:center; margin: 16px 0 8px; padding: 16px;
         background: var(--surface2); border: 1px solid var(--border);
         border-radius: 14px; animation: fadeSlideUp 0.6s ease both;">
      <div style="font-family:'Bebas Neue',sans-serif; font-size:1.2rem;
           letter-spacing:0.1em; color:var(--accent3); margin-bottom:6px;">
        🏆 STAY DISCIPLINED. STAY HUNGRY.
      </div>
      <div style="font-family:'Space Mono',monospace; font-size:0.65rem;
           letter-spacing:0.14em; text-transform:uppercase; color:var(--muted);">
        Results come to those who show up every single day
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("← Back", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
    with c2:
        st.markdown('<div class="cta-btn">', unsafe_allow_html=True)
        if st.button("🔄 Start Over ↻", use_container_width=True):
            st.session_state.step = 1
            st.session_state.user_df = None
            st.session_state.pred_bf = None
            st.session_state.bf_cat = None
            st.session_state.quote_idx = random.randint(0, len(GYM_QUOTES) - 1)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)