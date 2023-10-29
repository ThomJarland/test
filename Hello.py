# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd

st.title("Votre demande concerne :")
choice_home_type = st.empty()  # Espace vide pour afficher le choix du type de logement

if st.button("Appartement"):
    choice_home_type.write("Vous avez choisi : Appartement")

    st.title("Votre choix de résidence :")
    choice_residence_type = st.empty()  # Espace vide pour afficher le choix de résidence

    if st.button("Résidence principale"):
        choice_residence_type.write("Vous avez choisi : Résidence principale")
    if st.button("Résidence secondaire"):
        choice_residence_type.write("Vous avez choisi : Résidence secondaire")

if st.button("Maison"):
    choice_home_type.write("Vous avez choisi : Maison")

    st.title("Votre choix de résidence :")
    choice_residence_type = st.empty()  # Espace vide pour afficher le choix de résidence

    if st.button("Résidence principale"):
        choice_residence_type.write("Vous avez choisi : Résidence principale")
    if st.button("Résidence secondaire"):
        choice_residence_type.write("Vous avez choisi : Résidence secondaire")