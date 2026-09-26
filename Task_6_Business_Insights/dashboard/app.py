import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Netflix Intelligence | Task 6",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GLOBAL STYLE
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 85% 5%, rgba(229, 9, 20, 0.10), transparent 28%),
        radial-gradient(circle at 10% 25%, rgba(100, 70, 255, 0.06), transparent 25%),
        #070709;
    color: #f5f5f5;
}

/* Hide Streamlit chrome */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Main container */
.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #101014 0%, #09090c 100%);
    border-right: 1px solid #24242c;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

/* Sidebar text */
section[data-testid="stSidebar"] label {
    color: #b8b8c2 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

.sidebar-brand {
    text-align: center;
    padding: 12px 0 25px 0;
}

.sidebar-logo {
    width: 62px;
    height: 62px;
    margin: auto;
    border-radius: 18px;
    background: linear-gradient(145deg, #e50914, #9b0009);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 31px;
    box-shadow: 0 12px 35px rgba(229,9,20,0.25);
}

.sidebar-brand-title {
    margin-top: 13px;
    font-size: 21px;
    font-weight: 800;
    letter-spacing: 1px;
}

.sidebar-brand-sub {
    color: #e50914;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 4px;
}

.sidebar-section {
    color: #777781;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 25px 0 10px 0;
}

.sidebar-stat {
    background: #141419;
    border: 1px solid #25252d;
    border-radius: 10px;
    padding: 11px 13px;
    margin: 7px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.sidebar-stat span {
    color: #898992;
    font-size: 12px;
}

.sidebar-stat strong {
    color: #f4f4f5;
    font-size: 13px;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background: #141419 !important;
    border: 1px solid #292931 !important;
    border-radius: 9px !important;
}

/* Hero */
.hero {
    position: relative;
    overflow: hidden;
    border: 1px solid #292931;
    border-radius: 24px;
    padding: 42px 46px;
    margin-bottom: 25px;

    background:
        radial-gradient(
            circle at 90% 50%,
            rgba(229, 9, 20, 0.20),
            transparent 35%
        ),
        linear-gradient(
            120deg,
            #15151b 0%,
            #0d0d11 55%,
            #111116 100%
        );

    box-shadow: 0 20px 60px rgba(0,0,0,0.35);
}

.hero::after {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    right: -100px;
    top: -100px;
    border-radius: 50%;
    border: 1px solid rgba(229,9,20,0.18);

    box-shadow:
        0 0 0 35px rgba(229,9,20,0.025),
        0 0 0 70px rgba(229,9,20,0.018);
}

.hero-badge {
    display: inline-block;

    padding: 7px 12px;

    border-radius: 100px;

    background: rgba(229,9,20,0.10);

    border: 1px solid rgba(229,9,20,0.28);

    color: #ff555d;

    font-size: 10px;
    font-weight: 800;

    letter-spacing: 1.3px;
}

.hero-title {
    margin-top: 17px;

    font-size: clamp(36px, 5vw, 61px);

    line-height: 1;

    font-weight: 800;

    letter-spacing: -2.5px;

    color: #ffffff;
}

.hero-title span {
    color: #e50914;
}

.hero-subtitle {
    max-width: 780px;

    margin-top: 18px;

    color: #a5a5ae;

    font-size: 15px;

    line-height: 1.7;
}

.hero-meta {
    margin-top: 22px;

    color: #707079;

    font-size: 11px;

    font-weight: 600;

    letter-spacing: 0.7px;
}

/* Status pill */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #111116;
    border: 1px solid #292931;
    border-radius: 100px;
    padding: 9px 14px;
    color: #a9a9b2;
    font-size: 12px;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #35d07f;
    box-shadow: 0 0 10px rgba(53,208,127,.65);
}

/* Section */
.section-head {
    margin: 34px 0 15px 0;
}

.section-title {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -.5px;
}

.section-subtitle {
    color: #777780;
    font-size: 12px;
    margin-top: 4px;
}

/* KPI cards */
.kpi {
    background: linear-gradient(145deg, #15151b, #0e0e12);
    border: 1px solid #292931;
    border-radius: 17px;
    padding: 21px;
    min-height: 132px;
    transition: .2s ease;
}

.kpi:hover {
    border-color: #45454f;
    transform: translateY(-2px);
}

.kpi-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.kpi-label {
    color: #85858e;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .8px;
}

.kpi-icon {
    width: 31px;
    height: 31px;
    border-radius: 9px;
    background: rgba(229,9,20,.10);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
}

.kpi-value {
    font-size: 27px;
    font-weight: 800;
    margin-top: 17px;
    color: #ffffff;
}

.kpi-note {
    color: #6e6e77;
    font-size: 10px;
    margin-top: 5px;
}

/* Chart containers */
.chart-card {
    background: #101014;
    border: 1px solid #25252d;
    border-radius: 17px;
    padding: 6px;
    overflow: hidden;
}

/* Insight cards */
.insight {
    background:
        linear-gradient(145deg, #15151b, #0e0e12);
    border: 1px solid #292931;
    border-radius: 16px;
    padding: 21px;
    min-height: 155px;
}

.insight-tag {
    color: #e50914;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.insight-title {
    font-size: 15px;
    font-weight: 750;
    margin-top: 10px;
}

.insight-text {
    color: #85858e;
    font-size: 12px;
    line-height: 1.65;
    margin-top: 8px;
}

/* Prediction */
.prediction-card {
    background:
        radial-gradient(circle at 85% 20%, rgba(229,9,20,.13), transparent 35%),
        #101014;
    border: 1px solid #292931;
    border-radius: 18px;
    padding: 25px;
}

/* Info banner */
.info-banner {
    background: #111116;
    border: 1px solid #25252d;
    border-radius: 11px;
    padding: 12px 15px;
    color: #8e8e97;
    font-size: 12px;
}

/* Divider */
hr {
    border-color: #24242b !important;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid #292931;
    border-radius: 12px;
    overflow: hidden;
}

/* Buttons */
.stButton > button {
    background: #e50914;
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #f21a25;
    color: white;
}

/* Footer */
.footer {
    text-align: center;
    border-top: 1px solid #222229;
    margin-top: 50px;
    padding: 25px 0 5px 0;
    color: #55555e;
    font-size: 10px;
    letter-spacing: .4px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "cleaned_dataset.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

# ============================================================
# GLOBAL METRICS
# ============================================================

total_titles = len(df)

total_movies = (df["type"] == "Movie").sum()
total_tv = (df["type"] == "TV Show").sum()

movie_pct = round(total_movies / total_titles * 100, 2)
tv_pct = round(total_tv / total_titles * 100, 2)

top_genre = df["primary_genre"].value_counts().idxmax()
top_genre_count = df["primary_genre"].value_counts().max()

top_country = df["country"].value_counts().idxmax()
top_country_count = df["country"].value_counts().max()

top_rating = df["rating"].value_counts().idxmax()
top_rating_count = df["rating"].value_counts().max()

min_year = df["release_year"].min()
max_year = df["release_year"].max()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-logo">🎬</div>
        <div class="sidebar-brand-title">NETFLIX</div>
        <div class="sidebar-brand-sub">BUSINESS INTELLIGENCE</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section">Explore Data</div>',
        unsafe_allow_html=True
    )

    selected_type = st.selectbox(
        "Content Type",
        ["All"] + sorted(df["type"].dropna().unique().tolist())
    )

    selected_genre = st.selectbox(
        "Primary Genre",
        ["All"] + sorted(df["primary_genre"].dropna().unique().tolist())
    )

    selected_rating = st.selectbox(
        "Rating",
        ["All"] + sorted(df["rating"].dropna().unique().tolist())
    )

    st.markdown(
        '<div class="sidebar-section">Dataset Snapshot</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="sidebar-stat">
            <span>Total Titles</span>
            <strong>{total_titles:,}</strong>
        </div>

        <div class="sidebar-stat">
            <span>Movies</span>
            <strong>{total_movies:,}</strong>
        </div>

        <div class="sidebar-stat">
            <span>TV Shows</span>
            <strong>{total_tv:,}</strong>
        </div>

        <div class="sidebar-stat">
            <span>Years</span>
            <strong>{min_year}–{max_year}</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.caption(
        "Auspify Technologies\n"
        "Data Science Internship\n"
        "Task 6 • Business Insights"
    )


# ============================================================
# FILTER DATA
# ============================================================

filtered = df.copy()

if selected_type != "All":
    filtered = filtered[filtered["type"] == selected_type]

if selected_genre != "All":
    filtered = filtered[filtered["primary_genre"] == selected_genre]

if selected_rating != "All":
    filtered = filtered[filtered["rating"] == selected_rating]


# ============================================================
# HERO SECTION
# ============================================================

st.html("""
<div class="hero">
    <div class="hero-badge">AUSPIFY DATA SCIENCE INTERNSHIP</div>

    <div class="hero-title">
        Netflix <span>Intelligence</span>
    </div>

    <div class="hero-subtitle">
        A business-focused analytics dashboard exploring
        Netflix's content portfolio, genres, countries,
        ratings, growth patterns and content trends.
    </div>

    <div class="hero-meta">
        INTERACTIVE BUSINESS ANALYTICS
        &nbsp;&nbsp;•&nbsp;&nbsp;
        DATA VISUALIZATION
        &nbsp;&nbsp;•&nbsp;&nbsp;
        PREDICTIVE MODELING
    </div>
</div>
""")

st.markdown(
    f"""
    <div class="info-banner">
        <span class="status-dot"></span>
        &nbsp; Showing <b style="color:#fff;">{len(filtered):,}</b>
        of <b style="color:#fff;">{total_titles:,}</b> titles
        based on the selected filters.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">📊 Executive Overview</div>
        <div class="section-subtitle">
            Key portfolio metrics from the Netflix dataset
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-top">
                <div class="kpi-label">Total Titles</div>
                <div class="kpi-icon">🎬</div>
            </div>
            <div class="kpi-value">{total_titles:,}</div>
            <div class="kpi-note">Netflix catalog records</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k2:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-top">
                <div class="kpi-label">Movies</div>
                <div class="kpi-icon">🍿</div>
            </div>
            <div class="kpi-value">{total_movies:,}</div>
            <div class="kpi-note">{movie_pct}% of catalog</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k3:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-top">
                <div class="kpi-label">TV Shows</div>
                <div class="kpi-icon">📺</div>
            </div>
            <div class="kpi-value">{total_tv:,}</div>
            <div class="kpi-note">{tv_pct}% of catalog</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k4:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-top">
                <div class="kpi-label">Top Genre</div>
                <div class="kpi-icon">🔥</div>
            </div>
            <div class="kpi-value" style="font-size:20px;">
                {top_genre}
            </div>
            <div class="kpi-note">{top_genre_count:,} titles</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SECONDARY METRICS
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("🌍 Top Country", top_country, f"{top_country_count:,} titles")

with m2:
    st.metric("🔞 Common Rating", top_rating, f"{top_rating_count:,} titles")

with m3:
    st.metric("📅 Release Range", f"{min_year}–{max_year}")

with m4:
    st.metric("🔎 Filtered Records", f"{len(filtered):,}")


# ============================================================
# CONTENT MIX
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">🎥 Content Mix</div>
        <div class="section-subtitle">
            Distribution of Movies and TV Shows
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

c1, c2 = st.columns([1, 1.35])

type_counts = filtered["type"].value_counts().reset_index()
type_counts.columns = ["type", "count"]

with c1:

    fig = px.pie(
        type_counts,
        names="type",
        values="count",
        hole=.68
    )

    fig.update_traces(
        textinfo="percent+label",
        textfont_size=12,
        marker=dict(
            line=dict(color="#0b0b0f", width=3)
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=390,
        margin=dict(l=20, r=20, t=30, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        annotations=[
            dict(
                text=f"<b>{len(filtered):,}</b><br>Titles",
                x=.5,
                y=.5,
                font=dict(size=20, color="white"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:

    fig = px.bar(
        type_counts,
        x="type",
        y="count",
        text="count"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_dark",
        height=390,
        margin=dict(l=20, r=20, t=30, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="",
        yaxis_title="Titles",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# GENRES + COUNTRIES
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">🌎 Content Landscape</div>
        <div class="section-subtitle">
            Most represented genres and production countries
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

genre_counts = (
    filtered["primary_genre"]
    .value_counts()
    .head(10)
    .sort_values()
    .reset_index()
)

genre_counts.columns = ["genre", "count"]

with c1:

    fig = px.bar(
        genre_counts,
        x="count",
        y="genre",
        orientation="h",
        text="count"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        template="plotly_dark",
        height=470,
        margin=dict(l=20, r=55, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Titles",
        yaxis_title="",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)


country_counts = (
    filtered["country"]
    .value_counts()
    .head(10)
    .sort_values()
    .reset_index()
)

country_counts.columns = ["country", "count"]

with c2:

    fig = px.bar(
        country_counts,
        x="count",
        y="country",
        orientation="h",
        text="count"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        template="plotly_dark",
        height=470,
        margin=dict(l=20, r=55, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Titles",
        yaxis_title="",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# RATINGS
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">🔞 Rating Distribution</div>
        <div class="section-subtitle">
            Most frequently represented content ratings
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

rating_counts = (
    filtered["rating"]
    .value_counts()
    .head(10)
    .reset_index()
)

rating_counts.columns = ["rating", "count"]

fig = px.bar(
    rating_counts,
    x="rating",
    y="count",
    text="count"
)

fig.update_traces(textposition="outside")

fig.update_layout(
    template="plotly_dark",
    height=400,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Rating",
    yaxis_title="Titles",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)


# ============================================================
# CONTENT GROWTH
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">📈 Content Growth</div>
        <div class="section-subtitle">
            Year-by-year Netflix content additions
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

yearly = (
    filtered.groupby("added_year")
    .size()
    .reset_index(name="title_count")
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=yearly["added_year"],
        y=yearly["title_count"],
        mode="lines+markers",
        fill="tozeroy",
        line=dict(width=3),
        marker=dict(size=7),
        name="Titles Added"
    )
)

fig.update_layout(
    template="plotly_dark",
    height=450,
    margin=dict(l=20, r=20, t=25, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Year",
    yaxis_title="Titles Added",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)


# ============================================================
# MOVIE VS TV TREND
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">🎬 Movies vs TV Shows Over Time</div>
        <div class="section-subtitle">
            Historical content mix by year
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

year_type = (
    filtered
    .groupby(["added_year", "type"])
    .size()
    .reset_index(name="title_count")
)

fig = px.bar(
    year_type,
    x="added_year",
    y="title_count",
    color="type",
    barmode="group"
)

fig.update_layout(
    template="plotly_dark",
    height=450,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Year",
    yaxis_title="Titles Added",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">💡 Business Insights</div>
        <div class="section-subtitle">
            Key observations derived from the dataset
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

i1, i2, i3 = st.columns(3)

with i1:
    st.markdown(
        f"""
        <div class="insight">
            <div class="insight-tag">Content Mix</div>
            <div class="insight-title">
                Movies dominate the catalog
            </div>
            <div class="insight-text">
                Movies represent {movie_pct}% of the available
                records, compared with {tv_pct}% for TV Shows.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with i2:
    st.markdown(
        f"""
        <div class="insight">
            <div class="insight-tag">Genre</div>
            <div class="insight-title">
                {top_genre} leads the catalog
            </div>
            <div class="insight-text">
                {top_genre} is the most represented primary genre
                with {top_genre_count:,} titles.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with i3:
    st.markdown(
        f"""
        <div class="insight">
            <div class="insight-tag">Geography</div>
            <div class="insight-title">
                {top_country} has the largest representation
            </div>
            <div class="insight-text">
                The dataset contains {top_country_count:,} titles
                associated with {top_country}.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

i1, i2, i3 = st.columns(3)

with i1:
    st.markdown(
        f"""
        <div class="insight">
            <div class="insight-tag">Rating</div>
            <div class="insight-title">
                {top_rating} is the most common rating
            </div>
            <div class="insight-text">
                The rating appears across {top_rating_count:,}
                titles in the dataset.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with i2:
    st.markdown(
        f"""
        <div class="insight">
            <div class="insight-tag">Timeline</div>
            <div class="insight-title">
                Long historical coverage
            </div>
            <div class="insight-text">
                The catalog contains content released between
                {min_year} and {max_year}.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with i3:
    st.markdown(
        f"""
        <div class="insight">
            <div class="insight-tag">Current View</div>
            <div class="insight-title">
                Interactive filtering
            </div>
            <div class="insight-text">
                The current dashboard view contains
                {len(filtered):,} records after applying filters.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PREDICTIVE ANALYTICS
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">🔮 Predictive Analytics</div>
        <div class="section-subtitle">
            Machine learning models used to analyze and forecast Netflix content growth
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# PREPARE YEARLY CONTENT DATA
# ------------------------------------------------------------

ml_data = (
    df.groupby("added_year")
    .size()
    .reset_index(name="title_count")
)

ml_data = ml_data.dropna()

ml_data["added_year"] = pd.to_numeric(
    ml_data["added_year"],
    errors="coerce"
)

ml_data["title_count"] = pd.to_numeric(
    ml_data["title_count"],
    errors="coerce"
)

ml_data = (
    ml_data
    .dropna()
    .sort_values("added_year")
    .reset_index(drop=True)
)

# ------------------------------------------------------------
# TRAIN / TEST DATA
# ------------------------------------------------------------

X = ml_data[["added_year"]]
y = ml_data["title_count"]


if len(ml_data) >= 8:

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )


    # --------------------------------------------------------
    # LINEAR REGRESSION
    # --------------------------------------------------------

    linear_model = LinearRegression()

    linear_model.fit(
        X_train,
        y_train
    )

    linear_pred = linear_model.predict(X_test)


    # --------------------------------------------------------
    # RANDOM FOREST
    # --------------------------------------------------------

    rf_model = RandomForestRegressor(
        n_estimators=200,
        max_depth=6,
        random_state=42
    )

    rf_model.fit(
        X_train,
        y_train
    )

    rf_pred = rf_model.predict(X_test)


    # --------------------------------------------------------
    # MODEL METRICS
    # --------------------------------------------------------

    linear_mae = mean_absolute_error(
        y_test,
        linear_pred
    )

    linear_rmse = np.sqrt(
        mean_squared_error(
            y_test,
            linear_pred
        )
    )

    linear_r2 = r2_score(
        y_test,
        linear_pred
    )


    rf_mae = mean_absolute_error(
        y_test,
        rf_pred
    )

    rf_rmse = np.sqrt(
        mean_squared_error(
            y_test,
            rf_pred
        )
    )

    rf_r2 = r2_score(
        y_test,
        rf_pred
    )


    # --------------------------------------------------------
    # MODEL PERFORMANCE CARDS
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-subtitle" style="margin-bottom:15px;">
            Model performance on the chronological content-growth dataset
        </div>
        """,
        unsafe_allow_html=True
    )


    p1, p2 = st.columns(2)


    with p1:

        st.html(
            f"""
            <div class="prediction-card">

                <div class="insight-tag">
                    LINEAR REGRESSION
                </div>

                <div class="insight-title">
                    Baseline Growth Model
                </div>

                <div class="insight-text">

                    A linear regression model was trained using
                    Netflix content additions by year.

                    <br><br>

                    <b style="color:#ffffff;">
                        MAE
                    </b>
                    &nbsp; {linear_mae:,.2f}

                    <br>

                    <b style="color:#ffffff;">
                        RMSE
                    </b>
                    &nbsp; {linear_rmse:,.2f}

                    <br>

                    <b style="color:#ffffff;">
                        R²
                    </b>
                    &nbsp; {linear_r2:.3f}

                </div>

            </div>
            """,
        )


    with p2:

        st.html(
            f"""
            <div class="prediction-card">

                <div class="insight-tag">
                    RANDOM FOREST
                </div>

                <div class="insight-title">
                    Non-Linear Growth Model
                </div>

                <div class="insight-text">

                    A Random Forest regression model was evaluated
                    against the same test period.

                    <br><br>

                    <b style="color:#ffffff;">
                        MAE
                    </b>
                    &nbsp; {rf_mae:,.2f}

                    <br>

                    <b style="color:#ffffff;">
                        RMSE
                    </b>
                    &nbsp; {rf_rmse:,.2f}

                    <br>

                    <b style="color:#ffffff;">
                        R²
                    </b>
                    &nbsp; {rf_r2:.3f}

                </div>

            </div>
            """,
        )


    # --------------------------------------------------------
    # ACTUAL VS PREDICTED
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-head">
            <div class="section-title">
                📊 Actual vs Predicted
            </div>

            <div class="section-subtitle">
                Comparison of observed content additions with model predictions
            </div>
        </div>
        """,
    )


    prediction_df = pd.DataFrame(
        {
            "Year": X_test["added_year"].values,
            "Actual": y_test.values,
            "Linear Regression": linear_pred,
            "Random Forest": rf_pred
        }
    ).sort_values("Year")


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=prediction_df["Year"],
            y=prediction_df["Actual"],
            mode="lines+markers",
            name="Actual",
            line=dict(width=3),
            marker=dict(size=8)
        )
    )


    fig.add_trace(
        go.Scatter(
            x=prediction_df["Year"],
            y=prediction_df["Linear Regression"],
            mode="lines+markers",
            name="Linear Regression",
            line=dict(dash="dash", width=2)
        )
    )


    fig.add_trace(
        go.Scatter(
            x=prediction_df["Year"],
            y=prediction_df["Random Forest"],
            mode="lines+markers",
            name="Random Forest",
            line=dict(dash="dot", width=2)
        )
    )


    fig.update_layout(
        template="plotly_dark",
        height=450,
        margin=dict(
            l=20,
            r=20,
            t=25,
            b=20
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Year",
        yaxis_title="Titles Added",
        hovermode="x unified"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # FUTURE FORECAST
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-head">
            <div class="section-title">
                🔮 Future Content Growth Forecast
            </div>

            <div class="section-subtitle">
                Projected content additions based on the trained models
            </div>
        </div>
        """,
    )


    last_year = int(
        ml_data["added_year"].max()
    )


    future_years = np.arange(
        last_year + 1,
        last_year + 6
    )


    future_X = pd.DataFrame(
        {
            "added_year": future_years
        }
    )


    future_linear = linear_model.predict(
        future_X
    )


    future_rf = rf_model.predict(
        future_X
    )


    forecast_df = pd.DataFrame(
        {
            "Year": future_years,
            "Linear Regression": future_linear,
            "Random Forest": future_rf
        }
    )


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=forecast_df["Year"],
            y=forecast_df["Linear Regression"],
            mode="lines+markers",
            name="Linear Regression",
            line=dict(width=3)
        )
    )


    fig.add_trace(
        go.Scatter(
            x=forecast_df["Year"],
            y=forecast_df["Random Forest"],
            mode="lines+markers",
            name="Random Forest",
            line=dict(width=3)
        )
    )


    fig.update_layout(
        template="plotly_dark",
        height=430,
        margin=dict(
            l=20,
            r=20,
            t=25,
            b=20
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Forecast Year",
        yaxis_title="Predicted Titles",
        hovermode="x unified"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # FORECAST TABLE
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-subtitle">
            Five-year projected content additions
        </div>
        """,
        unsafe_allow_html=True
    )


    display_forecast = forecast_df.copy()

    display_forecast["Linear Regression"] = (
        display_forecast["Linear Regression"]
        .round(0)
        .astype(int)
    )

    display_forecast["Random Forest"] = (
        display_forecast["Random Forest"]
        .round(0)
        .astype(int)
    )


    st.dataframe(
        display_forecast,
        use_container_width=True,
        hide_index=True
    )


else:

    st.warning(
        "Not enough yearly data points are available to train the predictive models."
    )
    

# ============================================================
# BUSINESS RECOMMENDATIONS
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">💼 Business Recommendations</div>
        <div class="section-subtitle">
            Action-oriented recommendations derived from portfolio,
            genre, geographic and growth patterns
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


r1, r2, r3 = st.columns(3)


with r1:

    st.html(
        f"""
        <div class="insight">

            <div class="insight-tag">
                CONTENT STRATEGY
            </div>

            <div class="insight-title">
                Maintain a balanced content portfolio
            </div>

            <div class="insight-text">
                Movies currently represent
                <b style="color:#ffffff;">{movie_pct}%</b>
                of the catalog, while TV Shows represent
                <b style="color:#ffffff;">{tv_pct}%</b>.
                Content planning should monitor this mix while
                evaluating audience demand and engagement.
            </div>

        </div>
        """,
    )


with r2:

    st.html(
        f"""
        <div class="insight">

            <div class="insight-tag">
                GENRE STRATEGY
            </div>

            <div class="insight-title">
                Monitor demand around leading genres
            </div>

            <div class="insight-text">
                <b style="color:#ffffff;">{top_genre}</b>
                is the most represented primary genre with
                <b style="color:#ffffff;">{top_genre_count:,}</b>
                titles. Genre-level performance can help guide
                future acquisition and content planning.
            </div>

        </div>
        """,
    )


with r3:

    st.html(
        f"""
        <div class="insight">

            <div class="insight-tag">
                GLOBAL STRATEGY
            </div>

            <div class="insight-title">
                Evaluate geographic content opportunities
            </div>

            <div class="insight-text">
                <b style="color:#ffffff;">{top_country}</b>
                has the largest representation in the dataset
                with <b style="color:#ffffff;">{top_country_count:,}</b>
                titles. Geographic portfolio analysis can help
                identify markets requiring further diversification.
            </div>

        </div>
        """,
    )


r1, r2, r3 = st.columns(3)


with r1:

    st.html(
        f"""
        <div class="insight">

            <div class="insight-tag">
                AUDIENCE STRATEGY
            </div>

            <div class="insight-title">
                Track audience segments by rating
            </div>

            <div class="insight-text">
                <b style="color:#ffffff;">{top_rating}</b>
                is the most common rating with
                <b style="color:#ffffff;">{top_rating_count:,}</b>
                titles. Rating-level analysis can support
                audience segmentation and content planning.
            </div>

        </div>
        """,
    )


with r2:

    st.html(
        """
        <div class="insight">

            <div class="insight-tag">
                GROWTH STRATEGY
            </div>

            <div class="insight-title">
                Use forecasting for capacity planning
            </div>

            <div class="insight-text">
                Historical content-addition patterns and the
                predictive models can be monitored to support
                future content acquisition and portfolio planning.
            </div>

        </div>
        """,
    )


with r3:

    st.html(
        """
        <div class="insight">

            <div class="insight-tag">
                DATA STRATEGY
            </div>

            <div class="insight-title">
                Combine analytics with business metrics
            </div>

            <div class="insight-text">
                Catalog size alone does not measure content
                performance. Future analysis should combine
                portfolio data with engagement, retention and
                regional performance metrics.
            </div>

        </div>
        """,
    )



# ============================================================
# DATA TABLE
# ============================================================

st.markdown(
    """
    <div class="section-head">
        <div class="section-title">📋 Dataset Explorer</div>
        <div class="section-subtitle">
            Browse the filtered Netflix records
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

preview_cols = [
    "title",
    "type",
    "country",
    "release_year",
    "rating",
    "primary_genre",
    "duration"
]

st.dataframe(
    filtered[preview_cols].head(100),
    use_container_width=True,
    hide_index=True,
    height=430
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        NETFLIX INTELLIGENCE • BUSINESS INSIGHTS DASHBOARD
        <br>
        Auspify Technologies Data Science Internship • Task 6
    </div>
    """,
    unsafe_allow_html=True
)