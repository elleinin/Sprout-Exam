<template>
    <div class="wrapper">
        <div class="cont">
            <div class="register">
                <h3>Register Employee</h3>
                <form @submit.prevent="submit">
                    <div class="mb-3">
                        <label for="first_name" class="form-label">First Name:</label>
                        <input type="text" name="first_name" v-model="form.first_name" class="form-control" />
                    </div>
                    <div class="mb-3">
                        <label for="last_name" class="form-label">Last Name:</label>
                        <input type="text" name="last_name" v-model="form.last_name" class="form-control" />
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email:</label>
                        <input type="text" name="email" v-model="form.email" class="form-control" />
                    </div>
                    <div class="mb-3 form-group">
                        <label for="employee_type">Employee Type:</label>
                        <select name="employee_type" v-model="form.employee_type" class="form-control">
                        <option>Regular</option>
                        <option>Contractual</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
        <div class="cont">
            <div v-if="employeesData.length">
                <div v-for="employee in employeesData" :key="employee.id" class="employees">
                    <div class="card">
                        <div class="card-body">
                            <ul>
                                <li><strong>First Name:</strong> {{ employee.first_name }}</li>
                                <li><strong>Last Name:</strong> {{ employee.last_name }}</li>
                                <li> {{employee.employee_type}} Employee</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import employee from '../store/modules/employee';

export default defineComponent({
  name: 'Dashboard',
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        email: '',
        employee_type: ''
      },
      employeesData: [],
      employeeData: []
    };
  },
  created: function() {
    return employee.actions.getEmployees;
  },
  beforeMount: function() {
      this.employeesData = employee.getters.stateEmployees
  },
  updated: function() {
      this.employeesData = employee.getters.stateEmployees
      this.employee = employee.getters.stateEmployee
  },
  methods: {
    async submit() {
      await employee.actions.createEmployee(this.form, this.form.employee_type);
    },
    async load() {
        await employee.actions.getEmployees;
    }
  },
});
</script>