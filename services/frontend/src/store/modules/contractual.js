import axios from 'axios';

const state = {
    contractuals: [],
    contractual: []
};

const getters = {
    stateContractuals: state => state.contractuals,
    stateContractual: state => state.contractual
};

const actions = {
    async getContractuals({ commit }) {
        let { data } = await axios.get('contractuals');
        commit('setContractuals', data);
    },
    async getContractual({ commit }, id) {
        let { data } = await axios.get(`contractual/${id}`);
        commit('setContractual', data)
    },
    async updateContractual({}, data) {
        await axios.patch(`contractual/${user.id}`, data.form)
    }
};

const mutations = {
    setContractuals(state, contractuals) {
        state.contractuals = contractuals;
    },
    setContractual(state, contractual) {
        state.contractual = contractual;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};