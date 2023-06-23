import streamlit as st

class Motherboard:
    def __init__(self, power, connection):
        self.power = power
        self.connection = connection

class CPU:
    def __init__(self, power, connection):
        self.power = power
        self.connection = connection

# Creating three objects per class
motherboards = [
    Motherboard(power=500, connection='Socket A'),
    Motherboard(power=750, connection='Socket B'),
    Motherboard(power=1000, connection='Socket C')
]

cpus = [
    CPU(power=500, connection='Socket A'),
    CPU(power=1000, connection='Socket B'),
    CPU(power=750, connection='Socket C')
]


#state
if 'Motherboard' not in st.session_state:
    st.session_state['Motherboard'] = 0
if 'Cpu' not in st.session_state:
    st.session_state['Cpu'] = 0
if 'problempower' not in st.session_state:
    st.session_state['problempower'] = ''

st.title("Motherboard and CPU Comparison")


# Displaying buttons for motherboards
st.subheader("Motherboards")
for i, motherboard in enumerate(motherboards):

    if st.button(f"Motherboard {i+1}"):

        st.session_state['Motherboard'] = i

        # Checking if power values are the same
        if motherboard.power == cpus[i].power:
            st.subheader("power Result: OK")
        else:
            st.subheader("power Result: Not OK")

moth = st.session_state['Motherboard']


# Displaying buttons for CPUs
st.subheader("CPUs")
for i, cpu in enumerate(cpus):

    if st.button(f"CPU {i+1}"):

        st.session_state['Cpu'] = i

        # Checking if power values are the same
        if cpu.power == motherboards[moth].power:
            st.subheader("power Result: OK")
        else:
            st.subheader("power Result: Not OK")


st.subheader(f"CPU problems found:{st.session_state['problempower']}")
st.write(st.session_state['Motherboard'])