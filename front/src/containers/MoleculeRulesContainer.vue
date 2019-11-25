<template>
  <v-row v-scroll="onScroll" class="pa-8">
    <v-col
      v-for="(category, i) in ruleTypes"
      :key="category.key"
      cols="12"
      class="mt-3"
    >
      <span :id="'category-' + i" class="headline font-weight-bold">
        {{ category.label }}
      </span>
      <v-divider class="mt-2"></v-divider>
      <RuleCard
        v-for="rule in rules"
        :key="rule.id"
        class="mt-4"
        :rule="rule"
      />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

import { Rule, RuleTypeDefinition, RuleTypeDefinitions } from '@/models/rules'
import RuleCard from '@/components/rules/RuleCard.vue'

const rulesModule = namespace('rules')

@Component({
  components: {
    RuleCard,
  },
})
export default class MoleculeRulesContainer extends Vue {
  @rulesModule.State rules!: Rule[]
  @rulesModule.State ruleCreation!: boolean

  public rulesByType(type: string): Rule[] {
    return this.rules.filter((rule: Rule) => rule.category === type)
  }

  ruleTypes: RuleTypeDefinition[] = RuleTypeDefinitions
  @rulesModule.State ruleTypeScroll!: number
  @rulesModule.State ruleTypeScrollDisabled!: boolean
  @rulesModule.Mutation('updateRuleTypeScrollFromContainer')
  updateRuleTypeScroll!: (ruleType: number) => void

  @Watch('ruleTypeScroll')
  onCategoryScrollChange(newCategoryScroll: number): void {
    if (newCategoryScroll !== undefined && !this.ruleTypeScrollDisabled) {
      this.$vuetify.goTo('#category-' + newCategoryScroll, { offset: 20 })
    }
  }

  public onScroll(event: {
    target: { scrollingElement: { scrollTop: number } }
  }): void {
    let lastType = 0

    const scroll = event.target.scrollingElement.scrollTop
    this.ruleTypes.forEach((ruleType, index) => {
      const ruleElement = document.getElementById('category-' + index)
      if (ruleElement !== null) {
        const rulePosition = ruleElement.offsetTop
        if (scroll >= rulePosition) {
          lastType = index + 1
        }
      }
    })

    this.updateRuleTypeScroll(lastType)
  }
}
</script>

<style lang="scss" scoped></style>
