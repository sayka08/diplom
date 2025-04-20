<!-- frontend/src/App.vue -->
<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container">
        <router-link class="navbar-brand" to="/">Aldik</router-link>
        <div class="navbar-nav ms-auto">
          <router-link class="nav-link" to="/posts">Posts</router-link>
          <router-link class="nav-link" to="/profile" v-if="isAuthenticated">Profile</router-link>
          <router-link class="nav-link" to="/login" v-if="!isAuthenticated">Login</router-link>
          <router-link class="nav-link" to="/register" v-if="!isAuthenticated">Register</router-link>
          <button class="btn btn-outline-danger btn-sm" v-if="isAuthenticated" @click="logout">Logout</button>
        </div>
      </div>
    </nav>
    <div class="container mt-4">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('access_token');
    },
  },
  methods: {
    async logout() {
      try {
        await this.$axios.post('/logout');
        localStorage.removeItem('access_token');
        this.$router.push('/login');
      } catch (error) {
        console.error('Logout failed:', error);
      }
    },
  },
};
</script>