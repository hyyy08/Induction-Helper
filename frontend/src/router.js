import { createRouter, createWebHistory } from 'vue-router';
import SignupPage from './components/Signuppage.vue';
import InductionPage from './components/inductionPage.vue';
import NewStudentForm from './components/newStudentform.vue';
import Home from './components/home.vue';
import Reporting from './components/report.vue';
import UserProfile from './components/profilePage.vue';
import EquipmentList from './components/EquipmentList.vue';
import AddEquipment from './components/AddEquipment.vue';
import AddCategory from './components/AddCategory.vue';
import EditEquipment from './components/EditEquipment.vue';
import EditCategory from './components/EditCategory.vue';
import InductionList from './components/InductionList.vue';
import AddInduction from './components/AddInduction.vue';
import EditInduction from './components/EditInduction.vue';
import Login from './components/login.vue';
import UserAdd from './components/UserAdd.vue';
import StudentInduction from './components/StudentInduction.vue';
import CategoryList from './components/CategoryList.vue';

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/home',
    name: 'home',
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupPage
  },
  {
    path: '/inductions',
    name: 'inductions',
    component: InductionPage,
    meta: { requiresAuth: true }
  },
  {
    path: '/new-student',
    name: 'new-student',
    component: NewStudentForm,
    meta: { requiresAuth: true }
  },
  {
    path: '/reporting',
    name: 'reporting',
    component: Reporting,
    meta: { requiresAuth: true }
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserProfile,
    meta: { requiresAuth: true }
  },
  {
    path: '/equipment',
    name: 'equipment',
    component: EquipmentList,
    meta: { requiresAuth: true }
  },
  {
    path: '/addEquipment',
    name: 'addEquipment',
    component: AddEquipment,
    meta: { requiresAuth: true }
  },
  {
    path: '/editEquipment',
    name: 'editEquipment',
    component: EditEquipment,
    meta: { requiresAuth: true }
  },
  {
    path: '/inductionList',
    name: 'inductionList',
    component: InductionList,
    meta: { requiresAuth: true }
  },
  {
    path: '/addInduction',
    name: 'addInduction',
    component: AddInduction,
    meta: { requiresAuth: true }
  },
  {
    path: '/editInduction',
    name: 'editInduction',
    component: EditInduction,
    meta: { requiresAuth: true }
  },
  {
    path: '/useradd',
    name: 'useradd',
    component: UserAdd
  },
  {
    path: '/studentInduction',
    name: 'studentInduction',
    component: StudentInduction,
    meta: { requiresAuth: true }
  },
  {
    path: '/categoryList',
    name: 'categoryList',
    component: CategoryList,
    meta: { requiresAuth: true }
  },
  {
    path: '/addCategory',
    name: 'addCategory',
    component: AddCategory,
    meta: { requiresAuth: true }
  },
  {
    path: '/editCategory',
    name: 'editCategory',
    component: EditCategory,
    meta: { requiresAuth: true }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Navigation Guard
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router;