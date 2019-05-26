<!--Main 主要内容公共组件-->
<template>
  <div id="main">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'MainNav'
}
</script>

<style scoped>
  #main {
    height: 100%;
    width: 100%;
    opacity: 0.99;
  }

</style>
