import axios from 'axios';

const state = {
    regulars: null,
    regular: null
};

const getters = {
    stateRegulars: state => state.regulars,
    stateRegular: state => state.regular
};

const actions = {
    async getRegulars({ commit }) {
        let { data } = await axios.get('regulars');
        commit('setRegulars', data);
    },
    async getRegular({ commit }, id) {
        let { data } = await axios.get(`regular/${id}`);
        commit('setRegular', data)
    },
    async updateRegular({}, data) {
        await axios.patch(`regular/${user.id}`, data.form)
    }
};

const mutations = {
    setRegulars(state, regulars) {
        state.regulars = regulars;
    },
    setRegular(state, regular) {
        state.regular = regular;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};