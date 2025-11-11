import streamlit as st
import base64

st.set_page_config(page_title="Wind Turbine", layout="wide")

# 背景設定関数
def set_background(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    @keyframes scrolltopfix {{
        from {{ scroll-behavior: auto; }}
        to {{
            scroll-behavior: smooth;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# ページを切り替えるたびに scroll reset するCSSスニペット
def reset_scroll():
    st.markdown("""
    <style>
    html, body, [class*="stAppViewContainer"], [class*="main"] {{
        scroll-behavior: auto !important;
        overflow-y: auto !important;
    }}
    </style>
    <script>
    window.onload = function() {{
        document.querySelectorAll('.main')[0].scrollTo(0,0);
    }}
    </script>
    """, unsafe_allow_html=True)


# --- ホームページ ---
def home():
    set_background("canva_bg.png")
    
    reset_scroll()

    st.markdown("<h1 style='text-align:center; font-size:70px; color:white;'>Wind Turbine</h1>", unsafe_allow_html=True)
    
    
    # 追加部分：詳細説明
    st.markdown("""
    <div style='font-size:22px; line-height:1.6; color:white;'>
    
    <!-- Description -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px; margin-bottom:30px;'>
        <div style='flex:1;'>
            <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>Description</h2>
            <p>
            Wind turbines use wind power to rotate turbines, which then spin generators to generate electricity.  
            First, wind turbine blades, like airplane wings or helicopter rotor blades, are able to receive wind power and rotate.  
            Then, this rotational energy is converted into electricity.
            </p>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://www.azom.com/images/Article_Images/ImageForArticle_21371_16457084545525256.jpg' 
                 width='500' style='border-radius:15px;'>
            <p style='font-size:18px; color:#ccc; margin-top:10px;'>Wind turbine overview</p>
        </div>
    </div>
    
    <!-- Wind Turbine Blades -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px; margin-bottom:30px;'>
        <div style='flex:1;'>
            <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>Wind Turbine Blades</h2>
            <p>
            Wind turbines have large blades, which are essential for capturing wind energy.  
            The turbine brade are designed to create air plessure differences.
            So, as wind blows across the blades, the air pressure differences causes the blades to lift up, making the rotor spin.  
            The rotor is connected to a generator, which converts this mechanical rotation into electrical energy.
            </p>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://i.ytimg.com/vi/p5k2LhKBSgQ/maxresdefault.jpg' 
                 width='500' style='border-radius:15px;'>
            <p style='font-size:18px; color:#ccc; margin-top:10px;'>Wind turbine blade structure</p>
        </div>
    </div>
    
    <!-- Advantages -->
    <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>Advantages</h2>
    <ul>
    <li>No need to worry about depletion – Since wind power utilizes wind, unlike fossil fuels, there is no need to worry about the energy source running out.</li>
    <li>No greenhouse gas emissions during power generation – Since wind power rotates the turbines, no greenhouse gases are emitted.</li>
    <li>Can be placed anywhere– Small wind turbines can be installed in a garden or other area.</li>
    <li>Power generation is possible day and night – While solar power generation cannot generate electricity at night, wind turbines use wind power to generate electricity 24 hours a day.</li>
    </ul>
    
    <!-- Disadvantages -->
    <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>Disadvantages</h2>
    <ul>
    <li>Power generation is dependent on wind power – Unlike fossil fuels, wind turbines rely on natural forces, making power generation unstable.</li>
    <li>Noise concerns – Noise is a challenge with wind turbines, making them difficult to install in cities.</li>
    <li>Potential impact on wildlife – High-speed turbines can have an adverse effect on birds and other wildlifes.</li>
    </ul>
    
    </div>
    """, unsafe_allow_html=True)


    st.markdown("<br><hr><h2 style='text-align:center; color:white;'>Explore More</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("canva_col1.png", width="stretch")
        if st.button("Compareson with Other Renewable Energy", key="compare", width="stretch"):
            st.session_state.page = "compare"
            st.rerun()

    with col2:
        st.image("canva_col2.png", width="stretch")
        if st.button("Wind Turbine Structure", key="benefits", width="stretch"):
            st.session_state.page = "benefits"
            st.rerun()

    with col3:
        st.image("canva_col3.png", width="stretch")
        if st.button("Types of Wind Turbine", key="types", width="stretch"):
            st.session_state.page = "types"
            st.rerun()

# --- 他ページ ---
def compare_page():
    set_background("canvasolar_bg.jpg")

    st.header("Compareson with Other Renewable Energy")

    st.markdown("""
    <div style='font-size:22px; line-height:1.6; color:white;'>
    
    <!-- Wind Power -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px;'>
        <div style='flex:1;'>
            <h2 style='font-size:28px; font-weight:bold;'>Wind Power</h2>
            <p>Wind power generation uses motors to convert the kinetic energy of wind-driven blades into electrical energy.</p>
            <ul>
                <li><b>Advantages:</b> Generates electricity day and night, emits almost no CO₂, and has low operating costs.</li>
                <li><b>Disadvantages:</b> Unstable generation depending on wind power, possible noise concerns, visual impact on the land scape, and limited suitable locations.</li>
            </ul>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://caltechsites-prod-assets.s3.amazonaws.com/scienceexchange/images/wind-turbine-future-energy.width-600.jpg'
                 width='500' style='border-radius:15px;'>
        </div>
    </div>
    
    <br><hr><br>
    
    <!-- Solar Power -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px;'>
        <div style='flex:1;'>
            <h2 style='font-size:28px; font-weight:bold;'>Solar Power</h2>
            <p>Solar power generation converts light energy into electrical energy, similar to the process of photosynthesis in plants.</p>
            <ul>
                <li><b>Advantages:</b> Easy to install, low maintenance, and costs have dropped significantly.</li>
                <li><b>Disadvantages:</b> No generation at night or on cloudy days, requires large installation areas.</li>
            </ul>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://i0.wp.com/environment.umn.edu/wp-content/uploads/2020/10/alrawasmarwan_83477_12613114_photovoltaic-system-2742302_1920.jpg?fit=1920%2C1230&ssl=1'
                 width='500' style='border-radius:15px;'>
        </div>
    </div>
    
    <br><hr><br>
    
    <!-- Hydropower -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px;'>
        <div style='flex:1;'>
            <h2 style='font-size:28px; font-weight:bold;'>Hydropower</h2>
            <p>Hydroelectric power generation uses the power of water to turn turbines, which then converts the energy into electrical energy.</p>
            <ul>
                <li><b>Advantages:</b> Stable, continuous generation and long lifespan.</li>
                <li><b>Disadvantages:</b> Dam construction affects ecosystems and limited to certain areas.</li>
            </ul>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://www.ene100.jp/www/wp-content/uploads/2016/10/ph_mizu.jpg'
                 width='500' style='border-radius:15px;'>
        </div>
    </div>
    
    <br><hr><br>
    
    <!-- Geothermal Power -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px;'>
        <div style='flex:1;'>
            <h2 style='font-size:28px; font-weight:bold;'>Geothermal Power</h2>
            <p>Geothermal power generation converts the Earth's thermal energy, created by volcanic activity, into electrical energy.</p>
            <ul>
                <li><b>Advantages:</b> Generates power 24 hours a day with very low CO₂ emissions.</li>
                <li><b>Disadvantages:</b> High construction cost and location is limited to geothermal regions.</li>
            </ul>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://www.fujielectric.co.jp/about/example/detail/__icsFiles/afieldfile/2023/09/29/main_img71.jpg'
                 width='500' style='border-radius:15px;'>
        </div>
    </div>
    
    <br><hr><br>
    
    <!-- Biomass Power -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px;'>
        <div style='flex:1;'>
            <h2 style='font-size:28px; font-weight:bold;'>Biomass Power</h2>
            <p>Biomass power generation uses wood and other materials instead of fossil fuels to generate electricity.</p>
            <ul>
                <li><b>Advantages:</b> Reuses organic waste and provides relatively stable generation.</li>
                <li><b>Disadvantages:</b> Emits CO₂ when burned and requires resources and land for fuel.</li>
            </ul>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://www.mdpi.com/energies/energies-16-01783/article_deploy/html/images/energies-16-01783-g001.png'
                 width='500' style='border-radius:15px;'>
        </div>
    </div>
    
    <br><hr><br>
    
    <!-- Summary -->
    <h2 style='font-size:28px; font-weight:bold;'>Summary</h2>
    <p>
    Wind power is an environmentally friendly form of renewable energy, but like other renewable energy sources, it relies on nature to generate energy and is therefore unstable.
    It is important to make effective use of renewable energy sources by combining them and making sure that each one complements the other's shortcomings.
    For example, wind power can be used as backup power at night when solar power cannot be used.
    </p>
    
    </div>
    """, unsafe_allow_html=True)

    if st.button("Back to Home", width="content"):
        st.session_state.page = "home"
        st.rerun()

def benefits_page():
    set_background("canvawind_bg.png")

    st.header("Wind Turbine Structure")
    st.markdown("<h2 style='font-size:28px; font-weight:bold; color:white;'>How Wind Turbines Work</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style='font-size:22px; line-height:1.6; color:white;'>
        A wind turbine consists of blades that catch the wind, a rotor that converts it into electricity, and a tower that supports the structure. 
        A wind turbine converts the kinetic energy of the wind into electrical energy. 
        When the wind blows, it pushes against the turbine blades, causing them to rotate. 
        These blades are shaped like airplane wings and create a pressure difference that efficiently captures the wind.
        This causes the blades to lift up, and rotate when the wind hits. 
        The rotating blades turn a rotor that is connected to a main shaft, which drives a generator.
        Inside the generator, this rotation is converted into electricity.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("canvastructure_bg.png", caption="Diagram of a modern wind turbine", use_container_width=True)

    # 👇ここをカラムの外に移動
    st.markdown("""
    <h2 style='font-size:28px; font-weight:bold; color:white;'>Summary</h2>
    <div style='font-size:22px; line-height:1.6; color:white;'>
    Wind turbines convert wind power into rotational energy, which is then converted into electricity.
    This allows for the production of clean, renewable energy with minimal environmental impact.
    While individual units do not produce much electricity, they are inexpensive and can be installed in a variety of locations.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Back to Home", width="content"):
        st.session_state.page = "home"
        st.rerun()

def types_page():
    set_background("canvasky_bg.jpg")

    st.header("Types of Wind Turbines")
    st.markdown("""
    <div style='font-size:22px; line-height:1.6; color:white;'>

    <!--イントロ-->
    <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>Overview</h2>
    <p>
    Wind power generation can be categorized into four types: 
    <b>Onshore Wind Power</b>, <b>Offshore Wind Power</b>, 
    <b>Horizontal-axis Turbines</b>, and <b>Vertical-axis Turbines</b>.  
    These turbines all use wind energy to produce electricity, 
    but each has different advantages and disadvantages.
    </p>

    <br>

    <!--設置場所-->
    <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>1. Location</h2>

    <!-- 陸上風力発電 -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px; margin-bottom:30px;'>
        <div style='flex:1;'>
            <h3 style='font-size:24px; font-weight:bold;'>Onshore Wind Power</h3>
            <p>
            Onshore wind turbines are build on land and are the most common form of wind power generation.
            It is relatively easy to construct and maintain, and the cost of installation is lower than offshore types.
            However, wind turbines are making noise, so it can't be built in the city.
            It is just able to build windy places such as mountain passes or open plains.
            </p>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://ourfuture.energy/wp-content/uploads/2019/03/wind-turbines.jpeg' 
                 width='500' style='border-radius:15px;'>
        </div>
    </div>

    <!-- 洋上風力発電 -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px; margin-bottom:50px;'>
        <div style='flex:1;'>
            <h3 style='font-size:24px; font-weight:bold;'>Offshore Wind Power</h3>
            <p>
            Offshore wind power involves wind turbines installed over the sea.
            It is placed over the ocean where people are not present, the noise—a disadvantage of wind turbines—is less likely to affect people.
            So, people can do large-scale wind power generation.
            However, because construction requires ships at sea, costs are high, and durability capable of withstanding the marine environment is essential.
            </p>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://www.energy.gov/sites/default/files/styles/full_article_width/public/Turbine_Comparison.jpg?itok=2tmJtLXQ' 
                 width='500' style='border-radius:15px;'>
        </div>
    </div>

    <br>

    <!--風車の種類-->
    <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>2. Turbine Shaft Angle</h2>

    <!-- 水平軸型 -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px; margin-bottom:30px;'>
        <div style='flex:1;'>
            <h3 style='font-size:24px; font-weight:bold;'>Horizontal-axis Turbines</h3>
            <p>
            Horizontal-axis turbines are the most normal type of wind power generation, it looks like the propellers found in fans.
            They made of large blades connected to a generator and a tower supporting the structure.
            The blades rotate around a horizontal axis. This design is very efficient and widely used for power generation.
            Since this type can only capture wind from one direction, horizontal-axis turbines feature a mechanism to align the blade axis with the wind direction.
            </p>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://www.windsystemsmag.com/wp-content/uploads/2019/10/1019-CW-I1.jpg' 
                 width='500' style='border-radius:15px;'>
        </div>
    </div>

    <!-- 垂直軸型 -->
    <div style='display:flex; align-items:center; justify-content:space-between; gap:40px;'>
        <div style='flex:1;'>
            <h3 style='font-size:24px; font-weight:bold;'>Vertical-axis Turbines</h3>
            <p>
            Vertical-axis turbines are wind generators with a vertical rotation axis, and it looks like a mixer.
            It made by vertical blades connected to a generator and a support column holding the structure.
            The blades rotate around the vertical axis.
            This design is smaller than horizontal-axis turbines, causing less harm to animals like birds and generating less noise.
            Therefore, they are often built in urban areas.
            Also, this design can capture wind from various directions.
            However, their power generation capacity is lower than that of horizontal-axis turbines.
            </p>
        </div>
        <div style='flex:1; text-align:center;'>
            <img src='https://www.anthropocenemagazine.org/wp-content/uploads/2017/03/vawt.jpg' 
                 width='500' style='border-radius:15px;'>
        </div>
    </div>

    <br><br>

    <!--まとめ-->
    <h2 style='font-size:28px; font-weight:bold; margin-bottom:10px;'>Summary</h2>
    <p>
    Wind turbines come in various types depending on installation location and shaft orientation, each with its own advantages and disadvantages.
    To promote wind power generation, it is crucial for us to select the appropriate type for each specific location.
    For example, offshore wind power can be installed in shallow waters, onshore wind power in windy mountainous areas, and vertical-axis turbines in windy gaps between urban buildings.
    </p>

    </div>
    """, unsafe_allow_html=True)
    if st.button("Back to Home", width="content"):
        st.session_state.page = "home"
        st.rerun()

# --- ページ遷移管理 ---
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home()
elif st.session_state.page == "compare":
    compare_page()
elif st.session_state.page == "benefits":
    benefits_page()
elif st.session_state.page == "types":
    types_page()

