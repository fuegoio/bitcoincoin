<template>
  <RuleCreation></RuleCreation>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

import RuleCreation from '@/components/rules/RuleCreation.vue'

@Component({
  components: {
    RuleCreation,
  },
})
export default class RuleCreationContainer extends Vue {}
</script>

<style scoped></style>
