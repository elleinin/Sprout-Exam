import axios from 'axios';

const state = {
    user: null,
};

const actions = {
    async register({ dispatch }, form) {
        await axios.post('register', form);
        let UserForm = new FormData();
        UserForm.append('username', form.username);
        UserForm.append('password', form.password);
        await dispatch('logIn', UserForm);
    },
    async logIn(user) {
        await axios.post('login', user);
    },
    async logOut({ commit }) {
        let user = null;
        commit('logout', user);
    }
};

const mutations = {
    setUser(state, username) {
        state.user = username;
    },
    logout(state, user) {
        state.user = user;
    },
};

export default {
    state,
    actions,
    mutations
};