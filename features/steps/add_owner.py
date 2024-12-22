from behave import *


@given('I am on add owner page')
def function_1(context):
    context.page.goto('https://spring-petclinic-clone-2024.azurewebsites.net/owners/new')


@when('I populate all required fields')
def function_2(context):
    context.page.locator('input#firstName').fill('Emma')
    context.page.locator('input#lastName').fill('Edison')
    context.page.locator('input#address').fill('Street 123')
    context.page.locator('input#city').fill('Avon')
    context.page.locator('input#telephone').fill('1234567')


@when('I click on Save button')
def function_3(context):
    context.page.get_by_role(
        'button', name='Add Owner'
    ).click()


@then('I see owner info')
def function_4(context):
    result = context.page.inner_text('h2')

    assert result == 'Owner Information'
