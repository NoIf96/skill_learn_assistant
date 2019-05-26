<!--Footer 底部公共组件-->
<template>
  <div id="footer">
    <el-dropdown id="menu">
      <span class="el-dropdown-link">
        <el-button type="info" icon="el-icon-circle-plus" circle @click="handleClick()"></el-button>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>
          {{ user_name }}
        </el-dropdown-item>
        <el-dropdown-item>
          <i class="el-icon-circle-close" @click="onLogout()">登出</i>
        </el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
import AdminAuthApi from '@/apis/skill_learn_assistant/admin/AuthApi';
import OrdinaryAuthApi from '@/apis/skill_learn_assistant/ordinary/AuthApi';
export default {
  name: 'FooterNav',
  props: {
    user_type: String
  },
  data () {
    return {
      user_name: ''
    }
  },
  mounted: function () {
    this.getCurrentUser();
  },
  methods: {
    getCurrentUser: function () {
      let that = this;
      if (that.user_type === 'admin') {
        AdminAuthApi.getCurrentUser().then(function (result) {
          that.user_name = result.data.user_name;
        }).catch(function (error) {
          console.log(error);
        });
      }
      if (that.user_type === 'ordinary') {
        OrdinaryAuthApi.getCurrentUser().then(function (result) {
          that.user_name = result.data.user_name;
        }).catch(function (error) {
          console.log(error);
        });
      }
    },
    onLogout: function () {
      let that = this;
      if (that.user_type === 'admin') {
        AdminAuthApi.logout().then(function (result) {
          alert(result.data.msg);
          that.$store.dispatch('adminLogout');
          that.$router.replace('/skill_learn_assistant/admin/login');
        }).catch(function (error) {
          console.log(error);
        });
      }
      if (that.user_type === 'ordinary') {
        OrdinaryAuthApi.logout().then(function (result) {
          alert(result.data.msg);
          that.$store.dispatch('logout');
          that.$router.replace('/skill_learn_assistant/login');
        }).catch(function (error) {
          console.log(error);
        });
      }
    },
    handleClick () {
      this.getCurrentUser();
    }
  }
}
</script>

<style scoped>
  #footer {
    height: 100%;
    width: 100%;
    opacity: 0.9;
  }
  #menu {
    float: right;
  }
</style>
