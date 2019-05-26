import MainNav from '@/components/nav/MainNav'

import OrdinaryAuth from '@/views/skill_learn_assistant/ordinary/AuthView'
import RegisterAuth from '@/views/skill_learn_assistant/ordinary/RegisterView'

import OrdinaryIndex from '@/views/skill_learn_assistant/ordinary/index'
import OrdinaryIntroduce from '@/views/skill_learn_assistant/ordinary/introduce'

import SystemSkillLibrary from '@/views/skill_learn_assistant/ordinary/system_library/SkillView'
import SystemOccupationLibrary from '@/views/skill_learn_assistant/ordinary/system_library/OccupationView'

import UserSkillTreeLibrary from '@/views/skill_learn_assistant/ordinary/user_library/SkillTreeView'
import UserOccupationLibrary from '@/views/skill_learn_assistant/ordinary/user_library/OccupationView'

import RecommendSkill from '@/views/skill_learn_assistant/ordinary/recommend_system/SkillView'
import RecommendOccupation from '@/views/skill_learn_assistant/ordinary/recommend_system/OccupationView'

let ordinaryRouter = [
  {
    path: '/',
    name: 'ordinary_index',
    redirect: '/skill_learn_assistant/index'
  },
  {
    path: '/skill_learn_assistant/login',
    name: 'ordinary_login',
    component: OrdinaryAuth
  },
  {
    path: '/skill_learn_assistant/register',
    name: 'ordinary_register',
    component: RegisterAuth
  },
  {
    path: '/skill_learn_assistant',
    name: 'ordinary',
    meta: {
      requireAuth: true,
      type: 'ordinary'
    },
    component: OrdinaryIndex,
    redirect: '/skill_learn_assistant/index',
    children: [
      {
        path: '/skill_learn_assistant/index',
        name: '首页',
        meta: {
          requireAuth: true,
          type: 'ordinary'
        },
        components: {
          main: OrdinaryIntroduce
        },
        is_menu_show: true,
        is_leaf: true
      },
      {
        path: '/skill_learn_assistant/systemLibrary',
        name: '系统库',
        meta: {
          requireAuth: true,
          type: 'ordinary'
        },
        components: {
          main: MainNav
        },
        redirect: '/skill_learn_assistant/systemLibrary/skillLibrary',
        is_menu_show: true,
        children: [
          {
            path: '/skill_learn_assistant/systemLibrary/skillLibrary',
            name: '技能',
            meta: {
              requireAuth: true,
              type: 'ordinary'
            },
            component: SystemSkillLibrary,
            is_menu_show: true,
            is_leaf: true
          },
          {
            path: '/skill_learn_assistant/admin/systemLibrary/occupationLibrary',
            name: '职业',
            meta: {
              requireAuth: true,
              type: 'ordinary'
            },
            component: SystemOccupationLibrary,
            is_menu_show: true,
            is_leaf: true
          }
        ]
      },
      {
        path: '/skill_learn_assistant/userLibrary',
        name: '个人技能库',
        meta: {
          requireAuth: true,
          type: 'ordinary'
        },
        components: {
          main: MainNav
        },
        redirect: '/skill_learn_assistant/userLibrary',
        is_menu_show: true,
        children: [
          {
            path: '/skill_learn_assistant/userLibrary/skillLibrary',
            name: '技能',
            meta: {
              requireAuth: true,
              type: 'ordinary'
            },
            type: 'skill',
            component: UserSkillTreeLibrary,
            is_menu_show: true,
            is_leaf: true
          },
          {
            path: '/skill_learn_assistant/userLibrary/occupationLibrary',
            name: '职业',
            meta: {
              requireAuth: true,
              type: 'ordinary'
            },
            type: 'occupation',
            component: UserOccupationLibrary,
            is_menu_show: true,
            is_leaf: true
          }
        ]
      },
      {
        path: '/skill_learn_assistant/recommendSystem',
        name: '推荐预测',
        meta: {
          requireAuth: true,
          type: 'ordinary'
        },
        components: {
          main: MainNav
        },
        redirect: '/skill_learn_assistant/recommendSystem/skill',
        is_menu_show: true,
        children: [
          {
            path: '/skill_learn_assistant/recommendSystem/skill',
            name: '技能',
            meta: {
              requireAuth: true,
              type: 'ordinary'
            },
            component: RecommendSkill,
            is_menu_show: true,
            is_leaf: true
          },
          {
            path: '/skill_learn_assistant/recommendSystem/occupation',
            name: '职业',
            meta: {
              requireAuth: true,
              type: 'ordinary'
            },
            component: RecommendOccupation,
            is_menu_show: true,
            is_leaf: true
          }
        ]
      }
    ]
  }
];

export default ordinaryRouter;
