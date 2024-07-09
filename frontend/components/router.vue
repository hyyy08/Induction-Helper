// router.vue

<script>
import { createRouter, createWebHistory } from 'vue-router';

import InductionList from './views/InductionList.vue';
import AddInduction from './views/AddInduction.vue';
import EditInduction from './views/EditInduction.vue';

import EquipmentList from './views/EquipmentList.vue';
import AddEquipment from './views/AddEquipment.vue';
import EditEquipment from './views/EditEquipment.vue';

import TaskList from './views/TaskList.vue'; 
import AddTask from './views/AddTask.vue'; 
import EditTask from './views/EditTask.vue'; 

export default {
  setup() {
    const routes = [
      {
        path: '/induction',
        name: 'InductionList',
        component: InductionList
      },
      {
        path: '/add-induction',
        name: 'AddInduction',
        component: AddInduction
      },
      {
        path: '/edit-induction',
        name: 'EditInduction',
        component: EditInduction
      },
      {
        path: '/equipment',
        name: 'EquipmentList',
        component: EquipmentList
      },
      {
        path: '/add-equipment',
        name: 'AddEquipment',
        component: AddEquipment
      },
      {
        path: '/edit-equipment',
        name: 'EditEquipment',
        component: EditEquipment
      },
      {
        path: '/task',
        name: 'TaskList',
        component: TaskList
      },
      {
        path: '/add-task',
        name: 'AddTask',
        component: AddTask
      },
      {
        path: '/edit-task',
        name: 'EditTask',
        component: EditTask
      }
    ];

    const router = createRouter({
      history: createWebHistory(),
      routes
    });

    return { router };
  }
};
</script>