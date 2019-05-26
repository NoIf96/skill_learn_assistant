<template>
    <el-container id="whole" direction="vertical">
      <el-header id="header">
        <headerNav></headerNav>
      </el-header>
      <el-container>
        <asideNav v-bind:menu_type="menu_type"></asideNav>
        <el-container direction="vertical">
          <el-main>
            <router-view name="main"/>
          </el-main>
          <el-footer>
            <footerNav  v-bind:user_type="user_type"></footerNav>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
</template>

<script>
import headerNav from '@/components/nav/HeaderNav'
import asideNav from '@/components/nav/AsideNav'
import footerNav from '@/components/nav/FooterNav'
export default {
  name: 'index',
  data () {
    return {
      menu_type: 'admin',
      user_type: 'admin'
    }
  },
  components: {
    headerNav,
    asideNav,
    footerNav
  }
}
</script>

<style scoped>
  #whole {
    height: 100%;
    width: 100%;
    background: url('../../../assets/img/bg-6.png');
    background-size: cover;
  }
  #header {
    padding: 0 0
  }
</style>
