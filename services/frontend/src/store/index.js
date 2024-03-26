import { createStore } from "vuex";

import employee from './modules/employee';
import regular from './modules/regular';
import contractual from './modules/contractual';
import user from './modules/user';

export default createStore({
    modules: {
        employee,
        regular,
        contractual,
        user
    }
});