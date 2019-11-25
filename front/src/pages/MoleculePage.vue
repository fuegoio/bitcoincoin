<template>
  <v-row class="fill-height">
    <v-col cols="3" class="white elevation-3">
      <MoleculeRulesNavContainer />
    </v-col>
    <v-col cols="9" class="pa-0">
      <v-scroll-x-transition mode="out-in">
        <MoleculeRulesContainer v-if="!ruleCreation" />
        <MoleculeRuleCreationContainer v-else />
      </v-scroll-x-transition>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

import MoleculeRulesContainer from '@/containers/MoleculeRulesContainer.vue'
import MoleculeRulesNavContainer from '@/containers/MoleculeRulesNavContainer.vue'
import MoleculeRuleCreationContainer from '@/containers/MoleculeRuleCreationContainer.vue'

const rulesModule = namespace('rules')

@Component({
  components: {
    MoleculeRulesContainer,
    MoleculeRulesNavContainer,
    MoleculeRuleCreationContainer,
  },
})
export default class MoleculePage extends Vue {
  @rulesModule.State ruleCreation!: boolean
}
</script>

<style lang="scss" scoped></style>
