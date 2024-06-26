import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(
    page_icon="📱"
)


st.header("A Brief Analysis into the Semiconductor Industry")
st.caption("_By :blue[Ananya Salian]_")

st.write("This is a small passion project I have made regarding the Semiconductor Industry following recent events and news.\
         The aim of this project is to consolidate knowledge regarding this growing field, whilst building on my coding and financial\
         understanding. This project will also obtain Financial Data of a few Semiconductor Companies, chosen due to their market share and/or my own\
         personal interests.")

tab1, tab2 = st.tabs(["Semiconductor Company Locations", "Semiconductors: What are they?"])

with tab1:
    st.write("Interactive Map of Top 50 Public Semiconductor Companies")
    st.caption("This map plots out the location of the Top 50 Semiconductor Companies, ranked by market cap. _**Feel free to zoom in**_ , as clicking each location pin\
            will provide further information regarding the company, such as their name, state of origin, market cap, price per share and market share. (Values are shown in US$)")
    st.caption("_Please be informed that this is a static page, and as such, information from this page is only updated to **21/06/2024**. As such, data shown\
            on this web app may not be currently accurate_")
    # Read the data from the file

    data = []
    with open('scdatamshare.csv', 'r') as file:
        for line in file.readlines()[1:]:
            parts = line.strip().split(',')
            data.append({
                'Name': parts[0],
                'State': parts[1],
                'LAT': float(parts[2]),
                'LON': float(parts[3]),
                'MarketCap': float(parts[4]),
                'PricePerShare': float(parts[5]),
                'Mshare': float(parts[6])
            })

    # Sort the data by latitude and longitude
    sorted_data = sorted(data, key=lambda x: (x['LAT'], x['LON']))

    # Create a folium map centered at the mean latitude and longitude
    m = folium.Map(location=[sum([d['LAT'] for d in sorted_data]) / len(sorted_data),
                            sum([d['LON'] for d in sorted_data]) / len(sorted_data)],
                zoom_start=1)  # Adjust the zoom level here (lower value for more zoomed out)

    # Create a MarkerCluster layer
    marker_cluster = MarkerCluster().add_to(m)

    # Add markers to the map
    for d in sorted_data:
        strang = 0
        val = int(d['MarketCap'])
        if len(str(val)) <= 9:
            strang = "$" + str(round(val/1000000, 3)) + "M"
        elif len(str(val)) >= 10 and len(str(val)) <= 12:
            strang = "$" + str(round(val/1000000000, 3)) + "B"
        if len(str(val)) >= 13:
            strang = "$" + str(round(val/1000000000000, 3)) + "T"
        

        
        # Format the popup text with HTML for line breaks
        popup = f"<b>Name:</b> {d['Name']} <br> <b>State:</b> {d['State']}<br> <b>Market Cap:</b> {strang}<br> <b>Price Per Share:</b> ${d['PricePerShare']}<br><b>Market Share:</b> {d['Mshare']}%"
        # Create marker with popup
        folium.CircleMarker(
            location=[d['LAT'], d['LON']],
            radius=10,  # Radius of the circle marker
            color='white',  # Border color
            fill=True,
            fill_color='red',  # Fill color
            fill_opacity=0.9,
            popup=folium.Popup(popup, max_width=300)
        ).add_to(marker_cluster)


    # Display the map
    folium_static(m)

with tab2:
    st.write("All about semiconductors")
    st.caption("This explanation is to fully aid my understanding\
               regarding semiconductors, and the topics\
               leading up to it as I have not had the opportunity\
               to study this during my course yet. I have separated this explanation into\
               several sections, going into detail regarding\
               _Pentavalent and Trivalent Elements_, _P-nodes and N-nodes_, \
               _Diodes_ and _Triodes and Transistors_.")
    
    st.write("""A semiconductor is defined as a substance with a conductivity \
             that changes based on environmental factors.""")
    st.write("""However, this term\
              is generally used to refer to Integrated Circuits (ICs), also\
              known as computer chips, or simply, chips.""")
    st.write("""Semiconductor\
              substances, usually doped with trivalent (p-node) and\
              pentavalent (n-node) elements can be used to create NPN\
              transistors, consisting of an emitter, base and collector\
              section, where the p-node in this transistor amplifies electric\
              currents for faster, more efficient output. """)
    st.write("""An IC contains \
             thousands of transistors, as well as multiple other electronic\
              components such as resistors and capacitors. Said ICs perform \
             boolean logic, outputting binary code that serve as the building\
              blocks of modern electronic systems.\
             """)

    st.caption("Want more information on these topics? Take a look below.")
    with st.expander(label="Brief Explanation of Pentavalent & Trivalent Elements"):
        st.write("""
                 - Pentavalent elements refer to elements with a valence shell (outermost electron shell) containing 5 electrons. 
                 - Trivalent electrons refer to elements with a valence shell of 3 electrons.
                 """)
        st.image('P.png', caption="Pentavalent & Trivalent elements")
    with st.expander(label="Doping Semiconductors: P-nodes & N-nodes"):
        st.write("""
                 - **Doping Semiconductors**: To modify the conductivity of semiconductor elements, impurities, usually in the form of pentavalent or trivalent elements, are introduced into the crystal lattice of the semiconductor. These introduced elements are also referred to as dopants. Doped semiconductors with impurities introduced are also called _extrinsic_ semiconductors whereas pure semiconductors are called _intrinsic_ semiconductors. 
                 - **N-Type Semiconductors**: These are a type of extrinsic semiconductor compound where pentavalent elements have been introduced. The most common pentavalent elements used to dope semiconductors are bismuth, antimony, phosphorus and arsenic. When bonded with silicon, each pentavalent element has 1 extra, unbonded electron, resulting in free electrons, giving this field a negative charge, hence, _N-Node_. 
                 - **P-Type Semiconductors**: These are a type of extrinsic semiconductor compound where trivalent elements have been introduced. The most common trivalent elements to dope semiconductors with are boron and aluminium.  When bonded with silicon, each trivalent element present results in a hole in the crystal lattice, where the lattice is lacking electrons. As a result, there is a strong positive charge in this region, thus giving the name, _P-Node_. 
                 """)
        st.image('lattice.png', caption="Effects of doping on silicon crystal lattice")
    with st.expander(label="Diodes"):
        st.write("""
                 - Diodes are electric components that\
                  allow the flow of electricity in only \
                 1 direction. Consisting of one cathode \
                 (P-Node) and one anode (N-Node), with this\
                  diode connected to a battery via a circuit,\
                  shown in the Diagram 1.                
                 """)
        st.image('diodecir.png', caption="Diagram 1")
        st.write("Let's take a closer look at our diode, as shown in Diagram 2")
        st.image('orignode.png', caption="Diagram 2")
        st.write("""
                - The point at which the P-Node \
                 and the N-Node meet is called the \
                 PN junction
                - Here, free electrons from the negatively \
                 charged N-node are attracted to the positively \
                 charged compounds, or ‘holes’ in the P-node. \
                 These free electrons diffuse across the PN \
                 junction, filling the empty holes in the P-Node, \
                 as shown in Diagram 3.
                 """)
        st.image("attract.png", caption="Diagram 3")
        st.write("""
                - Over time, this results in the section \
                 of the P-Node near the PN junction being \
                 comparatively more negatively charged than \
                 the rest of the P-Node, and likewise with the \
                 N-Node. This resulting electric field opposes\
                  any further natural diffusion of electrons, \
                 and is called Depletion Region, demonstrated \
                 in the diagram 4. 
                 """)
        st.image("deplet.png", caption="Diagram 4")
        st.write("""
                - The depletion region is formed \
                 very quickly and though it is small, \
                 it expands very quickly, and continues \
                 to do so, until total negative charge \
                 in the N-Node of the Depletion Region \
                 repels any further electron diffusion \
                 across the PN junction (from the N \
                 region to P region). 
                - Now, let's zoom out and take a look at \
                 Diagram 1 again. Thanks to the battery \
                 that provides energy, the remaining free\
                  electrons are boosted with a voltage that\
                  is higher than the barrier potential of \
                 the depletion field, giving the free electrons \
                 a higher energy level, allowing them to cross\
                  and fill the other electron holes in the \
                 P-Node. As all the electrons are boosted to 
                 higher energy levels, they travel into the \
                 P-Node, as they are repelled from the negative\
                  end of the battery. At the P-Node, they are \
                 attracted to the positive end of the battery,\
                  causing them to flow to the positive terminal\
                  of the battery, thus resulting in a current\
                  flow only permitted in one direction.\
                  _(Diagram 3)_
                 """)
    with st.expander(label="Transistors"):
        st.write("Want to learn about transistors? I recommend this insightful youtube video, with excellent animations\
                 that provide a detailed explanation.")
        st.video("https://www.youtube.com/watch?v=7ukDKVHnac4",start_time="4m00s")
    

