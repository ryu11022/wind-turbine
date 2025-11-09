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

    if st.button("Back to Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
