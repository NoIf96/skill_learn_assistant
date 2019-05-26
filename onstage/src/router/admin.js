import MainNav from '@/components/nav/MainNav'

import AdminAuth from '@/views/skill_learn_assistant/admin/AuthView'
import AdminAdminUser from '@/views/skill_learn_assistant/admin/user/AdminView'
import AdminOrdinaryUser from '@/views/skill_learn_assistant/admin/user/OrdinaryView'
import AdminLibrarySkill from '@/views/skill_learn_assistant/admin/library/SkillView'
import AdminLibraryOccupation from '@/views/skill_learn_assistant/admin/library/OccupationView'
import AdminSystemConfig from '@/views/skill_learn_assistant/admin/system/ConfigView'

import AdminIndex from '@/views/skill_learn_assistant/admin/index'
import AdminIntroduce from '@/views/skill_learn_assistant/admin/introduce'

let adminRouter = [
  {
    path: '/skill_learn_assistant/admin/login',
    name: 'admin_login',
    component: AdminAuth
  },
  {
    path: '/skill_learn_assistant/admin',
    name: 'admin',
    meta: {
      requireAuth: true,
      type: 'admin'
    },
    component: AdminIndex,
    redirect: '/skill_learn_assistant/admin/index',
    children: [
      {
        path: '/skill_learn_assistant/admin/index',
        name: '首页',
        meta: {
          requireAuth: true,
          type: 'admin'
        },
        components: {
          main: AdminIntroduce
        },
        is_menu_show: true,
        is_leaf: true
      },
      {
        path: '/skill_learn_assistant/admin/userManger',
        name: '用户管理',
        meta: {
          requireAuth: true,
          type: 'admin'
        },
        components: {
          main: MainNav
        },
        redirect: '/skill_learn_assistant/admin/userManger/adminUser',
        is_menu_show: true,
        children: [
          {
            path: '/skill_learn_assistant/admin/userManger/adminUser',
            name: '管理员',
            meta: {
              requireAuth: true,
              type: 'admin'
            },
            component: AdminAdminUser,
            is_menu_show: true,
            is_leaf: true
          },
          {
            path: '/skill_learn_assistant/admin/userManger/commonUser',
            name: '普通用户',
            meta: {
              requireAuth: true,
              type: 'admin'
            },
            component: AdminOrdinaryUser,
            is_menu_show: true,
            is_leaf: true
          }
        ]
      },
      {
        path: '/skill_learn_assistant/admin/library',
        name: '系统库',
        meta: {
          requireAuth: true,
          type: 'admin'
        },
        components: {
          main: MainNav
        },
        redirect: '/skill_learn_assistant/admin/library/skill',
        is_menu_show: true,
        children: [
          {
            path: '/skill_learn_assistant/admin/library/skill',
            name: '系统技能库',
            meta: {
              requireAuth: true,
              type: 'admin'
            },
            type: 'skill',
            component: AdminLibrarySkill,
            is_menu_show: true,
            is_leaf: true
          },
          {
            path: '/skill_learn_assistant/admin/library/occupation',
            name: '系统职业库',
            meta: {
              requireAuth: true,
              type: 'admin'
            },
            type: 'occupation',
            component: AdminLibraryOccupation,
            is_menu_show: true,
            is_leaf: true
          }
        ]
      },
      {
        path: '/skill_learn_assistant/admin/recommendSystem',
        name: '推荐系统',
        meta: {
          requireAuth: true,
          type: 'admin'
        },
        components: {
          main: MainNav
        },
        redirect: '/skill_learn_assistant/admin/recommendSystem/option_skill',
        is_menu_show: true,
        children: [
          {
            path: '/skill_learn_assistant/admin/recommendSystem/option_skill',
            name: 'skill模型设置',
            meta: {
              requireAuth: true,
              type: 'admin',
              model_type: 'skill'
            },
            component: AdminSystemConfig,
            is_menu_show: true,
            is_leaf: true
          },
          {
            path: '/skill_learn_assistant/admin/recommendSystem/option_occupation',
            name: 'occupation模型设置',
            meta: {
              requireAuth: true,
              type: 'admin',
              model_type: 'occupation'
            },
            component: AdminSystemConfig,
            is_menu_show: true,
            is_leaf: true
          }
        ]
      }
    ]
  }
];

export default adminRouter;
