<template>
  <v-form class="px-3">
    Cash Flow = {{ user.cash_flow | toCurrency }}
    <v-text-field label="Amount"></v-text-field>
  </v-form>
</template>

<script>
export default {
  name: 'SellingForm',
  props: {
    currency: Object,
    volume: Float32Array,
  },
}
</script>

<style scoped></style>
