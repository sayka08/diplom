<template>
  <div class="register-container d-flex flex-column align-items-center justify-content-center">
    <!-- Заголовок Facebook -->
    <h1 class="facebook-title">aldik</h1>

    <!-- Карточка регистрации -->
    <div class="card register-card shadow p-3 mb-3 bg-white rounded">
      <h3 class="text-center mb-2">Создайте новый аккаунт</h3>
      <p class="text-center mb-4">Это быстро и просто.</p>

      <form @submit.prevent="onSubmit">
        <div class="mb-3">
          <input
            type="text"
            class="form-control"
            placeholder="Имя пользователя"
            v-model="username"
          />
        </div>

        <div class="mb-3">
          <input
            type="password"
            class="form-control"
            placeholder="Пароль"
            v-model="password"
          />
        </div>

        <button type="submit" class="btn btn-success w-100">
          Зарегистрироваться
        </button>
      </form>

      <div class="mt-3 text-center">
        <a href="#" @click.prevent="goToLogin" class="link-secondary">
          У вас уже есть аккаунт?
        </a>
      </div>
    </div>

    <!-- Сообщения об успехе / ошибке -->
    <div v-if="successMessage" class="alert alert-success mt-3">
      {{ successMessage }}
    </div>
    <div v-if="errorMessage" class="alert alert-danger mt-3">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

// Поля
const username = ref('')
const password = ref('')

// Для вывода сообщений
const successMessage = ref('')
const errorMessage = ref('')

// Роутер для редиректа
const router = useRouter()

async function onSubmit() {
  successMessage.value = ''
  errorMessage.value = ''

  try {
    // Запрос на бэкенд
    const response = await axios.post('http://localhost:8000/api/v1/register', {
      username: username.value,
      password: password.value
    })
    // Выводим сообщение об успехе
    successMessage.value = 'Успешно зарегистрированы: ' + response.data.username

    // Через 1 секунду редиректим на /login
    setTimeout(() => {
      router.push('/login')
    }, 1000)
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Error'
  }
}

// Ссылка «У вас уже есть аккаунт?» → /login
function goToLogin() {
  router.push('/login')
}
</script>

<style scoped>
.register-container {
  min-height: 100vh;
  background-color: #f0f2f5;
  padding: 2rem;
}

.facebook-title {
  font-size: 3.5rem;
  color: #1877f2;
  font-weight: bold;
  font-family: Helvetica, Arial, sans-serif;
  margin-bottom: 1rem;
}

.register-card {
  width: 400px;
  max-width: 90%;
}

/* Ссылка «У вас уже есть аккаунт?» */
.link-secondary {
  text-decoration: none;
  color: #606770;
}

.link-secondary:hover {
  text-decoration: underline;
}
</style>
