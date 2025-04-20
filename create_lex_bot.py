import boto3
import time

LEX_SERVICE_ROLE_ARN = 'arn:aws:iam::661256828619:role/Experience_Optimizer_POC'
REGION = 'us-west-2'

lex_client = boto3.client('lexv2-models', region_name=REGION)

# Step 1: Create the bot
bot_response = lex_client.create_bot(
    botName='BotFromPythonScript',
    description='Bot with BookHotel and OrderPizza intents',
    roleArn=LEX_SERVICE_ROLE_ARN,
    dataPrivacy={'childDirected': False},
    idleSessionTTLInSeconds=300
)
bot_id = bot_response['botId']
print(f"✅ Bot created: {bot_id}")

# Wait for bot to be fully created
print("⏳ Waiting for bot to be available...")
while True:
    bot_status = lex_client.describe_bot(botId=bot_id)
    status = bot_status['botStatus']
    print(f"   Bot status: {status}")
    if status == 'Available':
        break
    time.sleep(5)

# Step 2: Create Locale
locale_response = lex_client.create_bot_locale(
    botId=bot_id,
    botVersion='DRAFT',
    localeId='en_US',
    description='English (US)',
    nluIntentConfidenceThreshold=0.4
)
print("✅ Locale created")

# Wait for locale to be ready for intent creation
print("⏳ Waiting for locale to be ready for build...")
while True:
    locale_status = lex_client.describe_bot_locale(
        botId=bot_id,
        botVersion='DRAFT',
        localeId='en_US'
    )
    status = locale_status['botLocaleStatus']
    print(f"   Locale status: {status}")
    if status == 'NotBuilt':
        break
    time.sleep(5)

# Step 3: Create BookHotel Intent
lex_client.create_intent(
    botId=bot_id,
    botVersion='DRAFT',
    localeId='en_US',
    intentName='BookHotel',
    sampleUtterances=[
        {'utterance': 'I want to book a hotel'},
        {'utterance': 'Book a room for me'},
        {'utterance': 'Reserve a hotel'},
        {'utterance': 'Can you book a hotel for tonight?'},
        {'utterance': 'I need a hotel in New York'}
    ],
    intentClosingSetting={
        'closingResponse': {
            'messageGroups': [{
                'message': {
                    'plainTextMessage': {
                        'value': 'Your hotel has been booked!'
                    }
                }
            }],
            'allowInterrupt': True
        }
    }
)

# Step 3: Create OrderPizza Intent
lex_client.create_intent(
    botId=bot_id,
    botVersion='DRAFT',
    localeId='en_US',
    intentName='OrderPizza',
    sampleUtterances=[
        {'utterance': 'I want to order a pizza'},
        {'utterance': 'Order pizza for me'},
        {'utterance': 'Can I get a pepperoni pizza?'},
        {'utterance': 'I would like to order pizza'},
        {'utterance': 'Pizza delivery please'}
    ],
    intentClosingSetting={
        'closingResponse': {
            'messageGroups': [{
                'message': {
                    'plainTextMessage': {
                        'value': 'Your pizza order has been placed!'
                    }
                }
            }],
            'allowInterrupt': True
        }
    }
)

print("✅ Intents created")

# Optional: Wait for intents to be visible
print("⏳ Waiting for intents to be available...")
while True:
    intent_list = lex_client.list_intents(
        botId=bot_id,
        botVersion='DRAFT',
        localeId='en_US'
    )
    intent_names = [i['intentName'] for i in intent_list['intentSummaries']]
    print(f"📦 Intents registered so far: {intent_names}")
    if 'BookHotel' in intent_names and 'OrderPizza' in intent_names:
        break
    time.sleep(5)

# Step 4: Build the locale
print("🔨 Triggering build for locale...")
lex_client.build_bot_locale(
    botId=bot_id,
    botVersion='DRAFT',
    localeId='en_US'
)

# Wait for build to complete
print("⏳ Waiting for locale build to complete...")
while True:
    locale_status = lex_client.describe_bot_locale(
        botId=bot_id,
        botVersion='DRAFT',
        localeId='en_US'
    )
    status = locale_status['botLocaleStatus']
    print(f"   Build status: {status}")
    if status == 'Built':
        break
    time.sleep(5)

# Step 5: Create bot version
print("📌 Creating bot version...")
version_response = lex_client.create_bot_version(
    botId=bot_id,
    botVersionLocaleSpecification={
        'en_US': {
            'sourceBotVersion': 'DRAFT'
        }
    }
)
bot_version = version_response['botVersion']
print(f"✅ Bot version created: {bot_version}")

# Wait for version to be available
print("⏳ Waiting for version to be available...")
while True:
    versions = lex_client.list_bot_versions(botId=bot_id)
    version_ids = [v['botVersion'] for v in versions['botVersionSummaries']]
    print(f"   Versions available: {version_ids}")
    if bot_version in version_ids:
        break
    time.sleep(5)

# Step 6: Create bot alias
print("🎯 Creating bot alias...")
alias_response = lex_client.create_bot_alias(
    botAliasName='ProdAlias',
    botId=bot_id,
    botVersion=bot_version,
    botAliasLocaleSettings={
        'en_US': {
            'enabled': True
        }
    }
)
alias_id = alias_response['botAliasId']
print(f"✅ Bot alias created: {alias_id}")
