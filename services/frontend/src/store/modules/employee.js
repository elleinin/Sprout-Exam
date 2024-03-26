import axios from 'axios';

const state = {
    employees: [],
    employee: [],
};

const getters = {
    stateEmployees: state => state.employees,
    stateEmployee: state => state.employee,
};

const actions = {
    async createEmployee({ dispatch }, user, type) {
        await axios.post('register', user, type);
        await dispatch('getEmployees');
    },
    async getEmployees({ commit }) {
        let [data] = await axios.get(`employees`)
        commit('setEmployees', data);
    },
    async getEmployee({ commit }, id) {
        let [data] = await axios.get(`employee/${id}`);
        commit('setEmployee', data)
    },
    async updateEmployee({}, user) {
        await axios.patch(`employee/${user.id}`, user.form)
    },
    async deleteEmployee({}, id) {
        await axios.delete(`employee/${id}`)
    }
};

const mutations = {
    setEmployees(state, employees) {
        state.employees = employees;
    },
    setEmployee(state, employee) {
        state.employee = employee;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};