import Vue from 'vue'
import Vuex from 'vuex'
import { Module, VuexModule, Mutation } from 'vuex-module-decorators'

import rulesData from '../mock/rules.json'
import { Rule, RuleTypeDefinitions } from '@/models/rules'
import { Count } from '@/types/types'

Vue.use(Vuex)

// see https://github.com/championswimmer/vuex-module-decorators
@Module({ namespaced: true })
class RulesModules extends VuexModule {
  public molecule = 0
  public rules: Rule[] = rulesData.rules

  public get ruleTypes(): string[] {
    return RuleTypeDefinitions.map(x => x.label)
  }

  public ruleTypeScroll = 0
  public ruleTypeScrollDisabled = false

  @Mutation
  public updateRuleTypeScrollFromNav(ruleType: number): void {
    this.ruleTypeScroll = ruleType
    this.ruleTypeScrollDisabled = false
  }

  @Mutation
  public updateRuleTypeScrollFromContainer(ruleType: number): void {
    this.ruleTypeScroll = ruleType
    this.ruleTypeScrollDisabled = true
  }

  public get ruleTypesWithCounts(): Count<string>[] {
    return RuleTypeDefinitions.map(type => {
      const count = this.rules.filter(rule => rule.category === type.key).length

      return { value: type.label, count: count }
    })
  }

  public ruleCreation = false

  @Mutation
  public toggleRuleCreation(): void {
    this.ruleCreation = !this.ruleCreation
    if (this.ruleCreation) {
      this.ruleTypeScroll = -1
    } else {
      this.ruleTypeScroll = 0
    }
  }
}

export default new Vuex.Store({
  modules: {
    rules: RulesModules,
  },
})
