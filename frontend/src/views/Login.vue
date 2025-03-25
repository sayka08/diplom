<template>
  <div class="login-container d-flex flex-column flex-lg-row align-items-center justify-content-center">
    <!-- Левая часть: логотип + текст -->
    <div class="left-section text-center text-lg-start mb-4 mb-lg-0">
      <h1 class="facebook-title">aldik</h1>
      <p class="facebook-subtitle">
        Aldik помогает вам всегда оставаться на связи
        и общаться со своими знакомыми.
      </p>
    </div>

    <!-- Правая часть: форма входа + кнопка регистрации в одной карточке -->
    <div class="right-section">
      <div class="card shadow-sm p-3 mb-3 bg-white rounded" style="width: 360px;">
        <h3 class="text-center mb-2">Вход на Aldik</h3>
        <!-- Форма входа -->
        <form @submit.prevent="onSubmit">
          <div class="mb-3">
            <input
              type="text"
              class="form-control form-control-lg"
              placeholder="Имя пользователя"
              v-model="username"
            />
          </div>
          <div class="mb-3">
            <input
              type="password"
              class="form-control form-control-lg"
              placeholder="Пароль"
              v-model="password"
            />
          </div>
          <button type="submit" class="btn btn-primary btn-lg w-100">
            Вход
          </button>
        </form>

        <!-- Разделительная линия -->
        <hr />

        <!-- Кнопка «Создать новый аккаунт» -->
        <div class="text-center">
          <button
            class="btn btn-success btn-md mt-2"
            @click="goToRegister"
          >
            Создать новый аккаунт
          </button>
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
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const successMessage = ref('')
const router = useRouter()

async function onSubmit() {
  errorMessage.value = ''
  successMessage.value = ''

  try {
    // Пример запроса на бэкенд (логин)
    const response = await axios.post('http://localhost:8000/api/v1/login', {
      username: username.value,
      password: password.value
    })
    // Сохраняем токен
    localStorage.setItem('access_token', response.data.access_token)

    successMessage.value = 'Вход выполнен!'
    // Редирект на /profile через секунду
    setTimeout(() => {
      router.push('/profile')
    }, 1000)

  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Error'
  }
}

function goToRegister() {
  router.push('/register')
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  padding: 1rem;
  background-color: #f0f2f5;
}

.left-section {
  max-width: 600px;
  margin-right: 2rem;
}

.facebook-title {
  font-size: 3.5rem;
  color: #1877f2;
  font-weight: bold;
  font-family: Helvetica, Arial, sans-serif;
}

.facebook-subtitle {
  font-size: 1.2rem;
  color: #1c1e21;
  font-family: Helvetica, Arial, sans-serif;
}

.right-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card {
  border: none;
}

.form-control-lg {
  font-size: 1rem;
  padding: 0.75rem 1rem;
}

.btn-lg {
  font-size: 1rem;
  padding: 0.75rem 1rem;
}
</style>
